#!/usr/bin/env python3
"""
Advanced usage examples for Browser Agent
"""

import asyncio
from datetime import datetime, timedelta
from brouser_agent import BrowserAgent, Config
from brouser_agent.utils.scheduler import TaskScheduler, ScheduledTask, RealTimeMonitor
from brouser_agent.plugins.registry import PluginRegistry
from brouser_agent.plugins.base import PluginManager


async def example_scheduled_tasks():
    """Example: Schedule recurring tasks"""
    config = Config()
    config.headless = True
    
    agent = BrowserAgent(config)
    scheduler = TaskScheduler(agent)
    
    # Schedule daily task
    daily_task = ScheduledTask(
        id="daily_news_check",
        name="Check Daily News",
        prompt="Go to BBC News and take a screenshot of the homepage",
        browser="chrome",
        schedule_type="daily",
        schedule_time="09:00"
    )
    
    # Schedule interval task
    interval_task = ScheduledTask(
        id="system_check",
        name="System Health Check",
        prompt="Navigate to httpbin.org/get to test connectivity",
        browser="chrome",
        schedule_type="interval",
        schedule_time="30m"  # Every 30 minutes
    )
    
    # Add tasks to scheduler
    scheduler.add_task(daily_task)
    scheduler.add_task(interval_task)
    
    # Start scheduler
    scheduler.start_scheduler()
    
    print("📅 Scheduled tasks:")
    for task_status in scheduler.list_tasks():
        print(f"  - {task_status['name']}: {task_status['status']}")
        print(f"    Next run: {task_status['next_run']}")
    
    print("\n⏰ Scheduler running... (Press Ctrl+C to stop)")
    
    try:
        # Run for 60 seconds then stop
        await asyncio.sleep(60)
    except KeyboardInterrupt:
        pass
    finally:
        scheduler.stop_scheduler()
        agent.close()


async def example_real_time_monitoring():
    """Example: Real-time monitoring and event handling"""
    config = Config()
    
    agent = BrowserAgent(config)
    monitor = RealTimeMonitor(agent)
    
    # Event handlers
    def on_browser_error(event_type, data):
        print(f"🚨 Browser error detected: {data.get('error')}")
    
    def on_high_cpu(event_type, data):
        print(f"⚠️ High CPU usage: {data.get('cpu_percent')}%")
    
    def on_browser_healthy(event_type, data):
        print(f"✅ Browser healthy - Current URL: {data.get('url')}")
    
    # Register event handlers
    monitor.add_callback('browser_error', on_browser_error)
    monitor.add_callback('high_cpu_usage', on_high_cpu)
    monitor.add_callback('browser_healthy', on_browser_healthy)
    
    # Start monitoring
    monitor.start_monitoring()
    
    print("👁️ Real-time monitoring started...")
    
    # Execute some tasks while monitoring
    try:
        await agent.execute_task("Go to Google and search for 'AI automation'", "chrome")
        await asyncio.sleep(10)  # Let monitoring run
        
        # Trigger a manual event
        monitor.trigger_manual_event('custom_event', {'message': 'Manual test event'})
        
    except Exception as e:
        print(f"Task error: {e}")
    finally:
        monitor.stop_monitoring()
        agent.close()


async def example_plugin_system():
    """Example: Using the plugin system"""
    config = Config()
    
    # Initialize plugin registry and manager
    registry = PluginRegistry()
    plugin_manager = PluginManager()
    
    # Discover and load plugins
    discovered = registry.discover_plugins()
    print(f"🔌 Discovered plugins: {list(discovered.keys())}")
    
    # Load specific plugins
    for plugin_name in ['form_filler', 'ecommerce']:
        try:
            plugin = registry.load_plugin(plugin_name)
            plugin_manager.register_plugin(plugin)
            print(f"✅ Loaded plugin: {plugin_name}")
        except Exception as e:
            print(f"❌ Failed to load {plugin_name}: {e}")
    
    # List loaded plugins
    print("\n📋 Loaded plugins:")
    for name, info in plugin_manager.list_plugins().items():
        status = "✅ Enabled" if info['enabled'] else "❌ Disabled"
        print(f"  - {name}: {status}")
        print(f"    Description: {info['metadata'].description}")
    
    # Use plugins with agent
    agent = BrowserAgent(config)
    plugin_manager.initialize_all_plugins(agent, agent.automation)
    
    try:
        # Use form filler plugin
        form_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'message': 'Hello from Browser Agent!'
        }
        
        result = await plugin_manager.execute_with_plugin(
            'form_filler',
            {
                'action': 'fill_form',
                'form_data': form_data,
                'submit_after': False
            }
        )
        
        print(f"\n🔌 Plugin execution result: {result}")
        
    finally:
        plugin_manager.shutdown_all_plugins()
        agent.close()


async def example_error_handling_and_recovery():
    """Example: Advanced error handling and recovery"""
    config = Config()
    config.screenshot_on_error = True
    
    async with BrowserAgent(config) as agent:
        # Intentionally cause some errors to demonstrate handling
        
        print("🧪 Testing error handling...")
        
        # Test 1: Invalid URL
        result1 = await agent.execute_task(
            "Navigate to an invalid URL: this-is-not-a-valid-url",
            "chrome"
        )
        
        print(f"Invalid URL test: {'✅' if not result1.success else '❌'}")
        if result1.error_message:
            print(f"   Error: {result1.error_message}")
        
        # Test 2: Element not found
        result2 = await agent.execute_task(
            "Go to Google and click on an element that doesn't exist",
            "chrome"
        )
        
        print(f"Element not found test: {'✅' if not result2.success else '❌'}")
        
        # Test 3: Successful recovery
        result3 = await agent.execute_task(
            "Go to Google, search for 'test', and take a screenshot",
            "chrome"
        )
        
        print(f"Recovery test: {'✅' if result3.success else '❌'}")


async def example_concurrent_tasks():
    """Example: Running multiple tasks concurrently"""
    config = Config()
    config.headless = True
    
    # Define multiple tasks
    tasks = [
        ("Go to Google and search for 'Python'", "chrome"),
        ("Navigate to httpbin.org/get", "chrome"),
        ("Go to example.com and take a screenshot", "chrome")
    ]
    
    print("🔄 Running concurrent tasks...")
    
    # Create agents for each task
    agents = [BrowserAgent(config) for _ in tasks]
    
    try:
        # Run tasks concurrently
        async def run_single_task(agent, prompt, browser):
            return await agent.execute_task(prompt, browser)
        
        # Execute all tasks concurrently
        coroutines = [
            run_single_task(agent, prompt, browser)
            for agent, (prompt, browser) in zip(agents, tasks)
        ]
        
        results = await asyncio.gather(*coroutines, return_exceptions=True)
        
        # Display results
        for i, (result, (prompt, _)) in enumerate(zip(results, tasks)):
            if isinstance(result, Exception):
                print(f"Task {i+1}: ❌ Exception - {result}")
            else:
                status = "✅" if result.success else "❌"
                print(f"Task {i+1}: {status} - {prompt[:50]}...")
                
    finally:
        # Clean up all agents
        for agent in agents:
            agent.close()


def run_example(example_func):
    """Helper to run an async example"""
    print(f"\n🚀 Running {example_func.__name__}")
    print("=" * 60)
    
    try:
        asyncio.run(example_func())
    except KeyboardInterrupt:
        print("\n⏹️ Example interrupted by user")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    print("=" * 60)


if __name__ == "__main__":
    print("🤖 Browser Agent - Advanced Usage Examples")
    
    # Run examples (comment out any you don't want to run)
    run_example(example_scheduled_tasks)
    run_example(example_real_time_monitoring)
    run_example(example_plugin_system)
    run_example(example_error_handling_and_recovery)
    run_example(example_concurrent_tasks)
    
    print("\n🎉 All advanced examples completed!")