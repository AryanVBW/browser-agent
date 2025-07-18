import json
import logging
import asyncio
from typing import Dict, List, Any, Optional, Union
from dataclasses import dataclass
from enum import Enum
import openai
import anthropic
import google.generativeai as genai

from .config import Config
from .ai_processor import TaskStep, TaskPlan


class LLMProvider(Enum):
    OPENAI = "openai"
    CLAUDE = "claude"
    GEMINI = "gemini"


@dataclass
class LLMModel:
    provider: LLMProvider
    model_name: str
    display_name: str
    description: str
    max_tokens: int
    supports_functions: bool = True
    cost_per_1k_tokens: float = 0.0


class MultiLLMProcessor:
    """Enhanced AI processor supporting multiple LLM providers"""
    
    AVAILABLE_MODELS = [
        LLMModel(LLMProvider.OPENAI, "gpt-4", "GPT-4", "Most capable OpenAI model", 8192, True, 0.03),
        LLMModel(LLMProvider.OPENAI, "gpt-4-turbo", "GPT-4 Turbo", "Latest GPT-4 with higher context", 128000, True, 0.01),
        LLMModel(LLMProvider.OPENAI, "gpt-3.5-turbo", "GPT-3.5 Turbo", "Fast and efficient", 16385, True, 0.002),
        LLMModel(LLMProvider.CLAUDE, "claude-3-opus-20240229", "Claude 3 Opus", "Most powerful Claude model", 200000, False, 0.015),
        LLMModel(LLMProvider.CLAUDE, "claude-3-sonnet-20240229", "Claude 3 Sonnet", "Balanced performance", 200000, False, 0.003),
        LLMModel(LLMProvider.CLAUDE, "claude-3-haiku-20240307", "Claude 3 Haiku", "Fast and cost-effective", 200000, False, 0.00025),
        LLMModel(LLMProvider.GEMINI, "gemini-pro", "Gemini Pro", "Google's most capable model", 32000, False, 0.001),
        LLMModel(LLMProvider.GEMINI, "gemini-pro-vision", "Gemini Pro Vision", "Multimodal capabilities", 16000, False, 0.001),
    ]
    
    def __init__(self, config: Config):
        self.config = config
        self.logger = logging.getLogger(__name__)
        self.current_provider = LLMProvider.OPENAI
        self.current_model = "gpt-3.5-turbo"
        
        # Initialize clients
        self.openai_client = None
        self.claude_client = None
        self.gemini_client = None
        
        self._initialize_clients()
        self.system_prompt = self._create_system_prompt()
    
    def _initialize_clients(self):
        """Initialize all LLM clients"""
        try:
            # OpenAI
            if self.config.openai_api_key:
                openai.api_key = self.config.openai_api_key
                self.openai_client = openai
                self.logger.info("OpenAI client initialized")
            
            # Claude/Anthropic
            if hasattr(self.config, 'claude_api_key') and self.config.claude_api_key:
                self.claude_client = anthropic.Anthropic(api_key=self.config.claude_api_key)
                self.logger.info("Claude client initialized")
            
            # Gemini
            if hasattr(self.config, 'gemini_api_key') and self.config.gemini_api_key:
                genai.configure(api_key=self.config.gemini_api_key)
                self.gemini_client = genai
                self.logger.info("Gemini client initialized")
                
        except Exception as e:
            self.logger.error(f"Error initializing LLM clients: {e}")
    
    def get_available_models(self) -> List[LLMModel]:
        """Get list of available models based on configured API keys"""
        available = []
        
        for model in self.AVAILABLE_MODELS:
            if model.provider == LLMProvider.OPENAI and self.openai_client:
                available.append(model)
            elif model.provider == LLMProvider.CLAUDE and self.claude_client:
                available.append(model)
            elif model.provider == LLMProvider.GEMINI and self.gemini_client:
                available.append(model)
        
        return available
    
    def set_model(self, provider: LLMProvider, model_name: str):
        """Set the current model to use"""
        self.current_provider = provider
        self.current_model = model_name
        self.logger.info(f"Switched to {provider.value}: {model_name}")
    
    def get_current_model(self) -> Optional[LLMModel]:
        """Get current model information"""
        for model in self.AVAILABLE_MODELS:
            if model.provider == self.current_provider and model.model_name == self.current_model:
                return model
        return None
    
    async def process_prompt(self, user_prompt: str, context: Optional[Dict] = None) -> TaskPlan:
        """Process user prompt using the current LLM"""
        try:
            enhanced_prompt = self._enhance_prompt(user_prompt, context)
            
            if self.current_provider == LLMProvider.OPENAI:
                response = await self._process_with_openai(enhanced_prompt)
            elif self.current_provider == LLMProvider.CLAUDE:
                response = await self._process_with_claude(enhanced_prompt)
            elif self.current_provider == LLMProvider.GEMINI:
                response = await self._process_with_gemini(enhanced_prompt)
            else:
                raise ValueError(f"Unsupported provider: {self.current_provider}")
            
            return self._parse_task_plan(response)
            
        except Exception as e:
            self.logger.error(f"Error processing prompt with {self.current_provider.value}: {e}")
            raise
    
    async def _process_with_openai(self, prompt: str) -> Dict:
        """Process prompt with OpenAI"""
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": prompt}
        ]
        
        response = await openai.ChatCompletion.acreate(
            model=self.current_model,
            messages=messages,
            max_tokens=self.config.max_tokens,
            temperature=self.config.temperature
        )
        
        content = response.choices[0].message.content
        return json.loads(content)
    
    async def _process_with_claude(self, prompt: str) -> Dict:
        """Process prompt with Claude"""
        full_prompt = f"{self.system_prompt}\n\nHuman: {prompt}\n\nAssistant:"
        
        response = await asyncio.get_event_loop().run_in_executor(
            None,
            lambda: self.claude_client.completions.create(
                model=self.current_model,
                prompt=full_prompt,
                max_tokens_to_sample=self.config.max_tokens,
                temperature=self.config.temperature
            )
        )
        
        content = response.completion.strip()
        return json.loads(content)
    
    async def _process_with_gemini(self, prompt: str) -> Dict:
        """Process prompt with Gemini"""
        model = self.gemini_client.GenerativeModel(self.current_model)
        
        full_prompt = f"{self.system_prompt}\n\n{prompt}"
        
        response = await asyncio.get_event_loop().run_in_executor(
            None,
            lambda: model.generate_content(
                full_prompt,
                generation_config=genai.types.GenerationConfig(
                    max_output_tokens=self.config.max_tokens,
                    temperature=self.config.temperature
                )
            )
        )
        
        content = response.text
        return json.loads(content)
    
    def _create_system_prompt(self) -> str:
        """Create system prompt for task planning"""
        return """You are an intelligent web browser automation agent. Convert natural language instructions into detailed, executable browser automation steps.

Available Actions:
- navigate: Go to a specific URL
- click: Click on an element (button, link, etc.)
- type: Enter text into input fields
- select: Choose from dropdown menus
- scroll: Scroll the page up/down/to element
- wait: Wait for elements to load or conditions to be met
- screenshot: Take a screenshot for verification
- extract: Extract specific information from the page
- verify: Check if certain conditions are met

Element Targeting Methods:
- id: Element ID (id:search-button)
- class: CSS class name (class:submit-btn)
- xpath: XPath selector (xpath://button[text()='Submit'])
- css: CSS selector (css:.nav-link)
- text: Visible text content (text:Sign In)
- name: Element name attribute (name:username)

Response Format (JSON):
{
  "objective": "Clear description of what we're trying to achieve",
  "steps": [
    {
      "action": "action_name",
      "target": "element_selector_or_url",
      "value": "text_to_enter_or_option_to_select",
      "condition": "wait_condition_if_needed",
      "description": "Human readable description of this step"
    }
  ],
  "success_criteria": ["List of conditions that indicate task completion"],
  "estimated_time": estimated_seconds_to_complete
}

Guidelines:
1. Be specific with element selectors
2. Include wait conditions for dynamic content
3. Add verification steps to ensure actions succeeded
4. Handle potential errors and edge cases
5. Keep steps atomic and sequential
6. Use human-like interaction patterns"""
    
    def _enhance_prompt(self, user_prompt: str, context: Optional[Dict] = None) -> str:
        """Enhance user prompt with context information"""
        enhanced = f"User Request: {user_prompt}\n\n"
        
        if context:
            if 'current_url' in context:
                enhanced += f"Current Page: {context['current_url']}\n"
            
            if 'page_title' in context:
                enhanced += f"Page Title: {context['page_title']}\n"
            
            if 'available_elements' in context:
                enhanced += f"Visible Elements: {context['available_elements']}\n"
            
            if 'previous_actions' in context:
                enhanced += f"Previous Actions: {context['previous_actions']}\n"
        
        enhanced += "\nPlease provide a detailed step-by-step plan to accomplish this task in JSON format."
        
        return enhanced
    
    def _parse_task_plan(self, task_data: Dict) -> TaskPlan:
        """Parse task data into TaskPlan object"""
        steps = []
        for step_data in task_data.get('steps', []):
            step = TaskStep(
                action=step_data['action'],
                target=step_data.get('target'),
                value=step_data.get('value'),
                condition=step_data.get('condition'),
                description=step_data.get('description', '')
            )
            steps.append(step)
        
        return TaskPlan(
            objective=task_data['objective'],
            steps=steps,
            success_criteria=task_data.get('success_criteria', []),
            estimated_time=task_data.get('estimated_time', 0)
        )
    
    async def generate_response(self, user_message: str, context: Optional[Dict] = None) -> str:
        """Generate a conversational response (not a task plan)"""
        try:
            prompt = f"Respond conversationally to this user message: {user_message}"
            
            if self.current_provider == LLMProvider.OPENAI:
                messages = [
                    {"role": "system", "content": "You are a helpful AI assistant for browser automation. Respond naturally and helpfully."},
                    {"role": "user", "content": prompt}
                ]
                
                response = await openai.ChatCompletion.acreate(
                    model=self.current_model,
                    messages=messages,
                    max_tokens=500,
                    temperature=0.7
                )
                
                return response.choices[0].message.content
            
            elif self.current_provider == LLMProvider.CLAUDE:
                full_prompt = f"Human: {prompt}\n\nAssistant:"
                
                response = await asyncio.get_event_loop().run_in_executor(
                    None,
                    lambda: self.claude_client.completions.create(
                        model=self.current_model,
                        prompt=full_prompt,
                        max_tokens_to_sample=500,
                        temperature=0.7
                    )
                )
                
                return response.completion.strip()
            
            elif self.current_provider == LLMProvider.GEMINI:
                model = self.gemini_client.GenerativeModel(self.current_model)
                
                response = await asyncio.get_event_loop().run_in_executor(
                    None,
                    lambda: model.generate_content(prompt)
                )
                
                return response.text
                
        except Exception as e:
            self.logger.error(f"Error generating response: {e}")
            return f"I apologize, but I encountered an error: {str(e)}"