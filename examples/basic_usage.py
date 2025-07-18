#!/usr/bin/env python3
"""
Basic usage examples for Browser Agent
"""

import asyncio
from brouser_agent import BrowserAgent, Config


async def example_search_and_screenshot():
    """Example: Search for something and take a screenshot"""
    config = Config()
    config.headless = False  # Show browser window
    config.screenshot_on_error = True
    
    async with BrowserAgent(config) as agent:
        # Simple search task
        result = await agent.execute_task(
            "Go to Google and search for 'Python web scraping'",
            browser="chrome"
        )
        
        print(f"Task completed: {result.success}")
        if result.screenshots:
            print(f"Screenshots saved: {result.screenshots}")


async def example_form_filling():
    """Example: Fill out a contact form"""
    config = Config()
    
    async with BrowserAgent(config) as agent:
        # Form filling task
        result = await agent.execute_task(
            """
            Go to https://httpbin.org/forms/post and fill out the form with:
            - Customer name: John Doe
            - Telephone: 555-0123
            - Email: john@example.com
            - Subject: Test Message
            - Message: This is a test message from Browser Agent
            Then submit the form
            """,
            browser="chrome"
        )
        
        print(f"Form filling completed: {result.success}")
        if not result.success:
            print(f"Error: {result.error_message}")


async def example_ecommerce():
    """Example: E-commerce product search"""
    config = Config()
    
    async with BrowserAgent(config) as agent:
        # E-commerce task
        result = await agent.execute_task(
            "Go to Amazon and search for 'wireless bluetooth headphones', then show me the first 3 results",
            browser="chrome"
        )
        
        print(f"E-commerce search completed: {result.success}")
        print(f"Steps executed: {len(result.step_results)}")


async def example_multiple_browsers():
    """Example: Test with multiple browsers"""
    browsers = ["chrome", "firefox"]  # Add more as available
    
    for browser in browsers:
        try:
            print(f"\n--- Testing with {browser} ---")
            
            config = Config()
            config.headless = True  # Run headless for speed
            
            async with BrowserAgent(config) as agent:
                result = await agent.execute_task(
                    "Go to https://httpbin.org/get and verify the page loads",
                    browser=browser
                )
                
                print(f"{browser}: {'✅ Success' if result.success else '❌ Failed'}")
                if not result.success:
                    print(f"Error: {result.error_message}")
                    
        except Exception as e:
            print(f"{browser}: ❌ Error - {e}")


async def example_with_plugins():
    """Example: Using plugins for specialized tasks"""
    config = Config()
    config.plugins_enabled = True
    
    async with BrowserAgent(config) as agent:
        # This would use the form filler plugin
        result = await agent.execute_task(
            "Fill out a registration form with sample data",
            browser="chrome"
        )
        
        print(f"Plugin-assisted task: {result.success}")


def run_example(example_func):
    """Helper to run an async example"""
    print(f"\n🚀 Running {example_func.__name__}")
    print("-" * 50)
    
    try:
        asyncio.run(example_func())
    except Exception as e:
        print(f"❌ Error: {e}")
    
    print("-" * 50)


if __name__ == "__main__":
    print("🤖 Browser Agent - Basic Usage Examples")
    
    # Run examples
    run_example(example_search_and_screenshot)
    run_example(example_form_filling)
    run_example(example_ecommerce)
    run_example(example_multiple_browsers)
    run_example(example_with_plugins)
    
    print("\n✅ All examples completed!")