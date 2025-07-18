import asyncio
import logging
import time
from typing import Dict, Any, Optional, List
from dataclasses import dataclass

from .config import Config
from .multi_llm_processor import MultiLLMProcessor, TaskPlan, TaskStep
from ..browsers.manager import BrowserManager
from ..utils.automation import WebAutomation
from ..utils.logger import setup_logging


@dataclass
class ExecutionResult:
    success: bool
    step_results: List[Dict[str, Any]]
    error_message: Optional[str] = None
    screenshots: List[str] = None
    execution_time: float = 0.0


class BrowserAgent:
    """Main browser automation agent with AI capabilities"""
    
    def __init__(self, config: Optional[Config] = None):
        self.config = config or Config()
        self.config.validate()
        
        # Setup logging
        self.logger = setup_logging(self.config.log_level, self.config.log_file)
        
        # Initialize components
        self.ai_processor = MultiLLMProcessor(self.config)
        self.browser_manager = BrowserManager(
            headless=self.config.headless,
            framework=self.config.automation_framework
        )
        self.automation = None
        self.current_task = None
        
    async def execute_task(self, user_prompt: str, browser: str = None) -> ExecutionResult:
        """Execute a task based on user prompt"""
        start_time = time.time()
        browser = browser or self.config.default_browser
        
        try:
            self.logger.info(f"Starting task: {user_prompt}")
            
            # Launch browser if not already running
            if not self.browser_manager.active_driver:
                driver = self.browser_manager.launch_browser(browser)
                self.automation = WebAutomation(driver, self.config)
            
            # Process user prompt into task plan
            context = await self._get_current_context()
            task_plan = await self.ai_processor.process_prompt(user_prompt, context)
            self.current_task = task_plan
            
            self.logger.info(f"Generated plan with {len(task_plan.steps)} steps")
            
            # Execute task plan
            execution_result = await self._execute_task_plan(task_plan)
            execution_result.execution_time = time.time() - start_time
            
            return execution_result
            
        except Exception as e:
            self.logger.error(f"Task execution failed: {e}")
            return ExecutionResult(
                success=False,
                step_results=[],
                error_message=str(e),
                execution_time=time.time() - start_time
            )
    
    async def _execute_task_plan(self, task_plan: TaskPlan) -> ExecutionResult:
        """Execute the task plan step by step"""
        step_results = []
        screenshots = []
        
        self.logger.info(f"Executing task: {task_plan.objective}")
        
        for i, step in enumerate(task_plan.steps):
            try:
                self.logger.info(f"Step {i+1}/{len(task_plan.steps)}: {step.description}")
                
                # Execute the step
                step_result = await self._execute_step(step)
                step_results.append(step_result)
                
                # Take screenshot if configured or on error
                if self.config.screenshot_on_error or step_result.get('screenshot_requested'):
                    screenshot_path = await self.automation.take_screenshot(
                        f"step_{i+1}_{step.action}"
                    )
                    if screenshot_path:
                        screenshots.append(screenshot_path)
                
                # Check if step failed
                if not step_result.get('success', True):
                    error_msg = step_result.get('error', 'Step execution failed')
                    self.logger.error(f"Step {i+1} failed: {error_msg}")
                    
                    # Try to recover or adapt plan
                    if not await self._handle_step_failure(step, step_result, i):
                        return ExecutionResult(
                            success=False,
                            step_results=step_results,
                            error_message=f"Step {i+1} failed: {error_msg}",
                            screenshots=screenshots
                        )
                
                # Human-like delay between steps
                if self.config.human_like_delays:
                    await asyncio.sleep(
                        self.config.min_delay + 
                        (self.config.max_delay - self.config.min_delay) * 0.5
                    )
                    
            except Exception as e:
                self.logger.error(f"Error executing step {i+1}: {e}")
                step_results.append({
                    'success': False,
                    'error': str(e),
                    'step': step.action
                })
                
                if self.config.screenshot_on_error:
                    screenshot_path = await self.automation.take_screenshot(f"error_step_{i+1}")
                    if screenshot_path:
                        screenshots.append(screenshot_path)
                
                return ExecutionResult(
                    success=False,
                    step_results=step_results,
                    error_message=f"Exception in step {i+1}: {e}",
                    screenshots=screenshots
                )
        
        # Verify success criteria
        success = await self._verify_success_criteria(task_plan.success_criteria)
        
        return ExecutionResult(
            success=success,
            step_results=step_results,
            screenshots=screenshots
        )
    
    async def _execute_step(self, step: TaskStep) -> Dict[str, Any]:
        """Execute a single step"""
        try:
            if step.action == "navigate":
                return await self.automation.navigate(step.target)
            
            elif step.action == "click":
                return await self.automation.click_element(step.target)
            
            elif step.action == "type":
                return await self.automation.type_text(step.target, step.value)
            
            elif step.action == "select":
                return await self.automation.select_option(step.target, step.value)
            
            elif step.action == "scroll":
                return await self.automation.scroll(step.target, step.value)
            
            elif step.action == "wait":
                return await self.automation.wait_for_element(step.target, step.condition)
            
            elif step.action == "screenshot":
                screenshot_path = await self.automation.take_screenshot(step.value or "manual")
                return {
                    'success': True,
                    'screenshot_path': screenshot_path,
                    'screenshot_requested': True
                }
            
            elif step.action == "extract":
                return await self.automation.extract_data(step.target, step.value)
            
            elif step.action == "verify":
                return await self.automation.verify_condition(step.target, step.value)
            
            else:
                return {
                    'success': False,
                    'error': f"Unknown action: {step.action}"
                }
                
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'action': step.action
            }
    
    async def _handle_step_failure(self, step: TaskStep, result: Dict, step_index: int) -> bool:
        """Handle step failure and attempt recovery"""
        # Simple retry logic for now
        retry_actions = ['click', 'type', 'select']
        
        if step.action in retry_actions:
            self.logger.info(f"Retrying step {step_index + 1}: {step.action}")
            await asyncio.sleep(2)  # Wait before retry
            
            retry_result = await self._execute_step(step)
            if retry_result.get('success'):
                self.logger.info(f"Step {step_index + 1} succeeded on retry")
                return True
        
        return False
    
    async def _verify_success_criteria(self, criteria: List[str]) -> bool:
        """Verify that success criteria are met"""
        for criterion in criteria:
            try:
                # This is a simplified verification
                # In a real implementation, you'd parse the criterion and check accordingly
                result = await self.automation.verify_condition(criterion)
                if not result.get('success'):
                    self.logger.warning(f"Success criterion not met: {criterion}")
                    return False
            except Exception as e:
                self.logger.error(f"Error verifying criterion '{criterion}': {e}")
                return False
        
        return True
    
    async def _get_current_context(self) -> Dict[str, Any]:
        """Get current browser context for AI processing"""
        if not self.automation:
            return {}
        
        try:
            context = {
                'current_url': await self.automation.get_current_url(),
                'page_title': await self.automation.get_page_title(),
            }
            
            # Get page content for analysis (limited to avoid token limits)
            page_source = await self.automation.get_page_source()
            if page_source:
                page_analysis = self.ai_processor.analyze_page_content(
                    page_source[:10000],  # Limit content size
                    context['current_url']
                )
                context.update(page_analysis)
            
            return context
            
        except Exception as e:
            self.logger.error(f"Error getting context: {e}")
            return {}
    
    def get_available_browsers(self) -> Dict[str, Any]:
        """Get list of available browsers"""
        return self.browser_manager.get_available_browsers()
    
    def switch_browser(self, browser_name: str):
        """Switch to a different browser"""
        if self.browser_manager.active_driver:
            self.browser_manager.close_browser()
        
        driver = self.browser_manager.launch_browser(browser_name)
        self.automation = WebAutomation(driver, self.config)
    
    def close(self):
        """Clean up resources"""
        if self.browser_manager:
            self.browser_manager.close_browser()
        self.logger.info("Browser agent closed")
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()