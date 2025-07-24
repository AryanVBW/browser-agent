#!/usr/bin/env python3
"""
Test script for unified browser and desktop automation
"""

import asyncio
import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from brouser_agent.utils.unified_automation import UnifiedAutomation
from brouser_agent.utils.desktop_automation import DesktopAutomation
from brouser_agent.utils.automation import WebAutomation
from brouser_agent.core.config import Config

async def test_desktop_automation():
    """Test desktop automation features"""
    print("🖥️ Testing Desktop Automation...")
    
    config = Config()
    desktop = DesktopAutomation(config)
    
    try:
        # Test screenshot
        print("📸 Taking screenshot...")
        result = await desktop.take_screenshot()
        print(f"Screenshot result: {result}")
        
        # Test mouse position
        print("🖱️ Getting mouse position...")
        result = await desktop.get_mouse_position()
        print(f"Mouse position: {result}")
        
        # Test screen info
        print("📊 Getting screen info...")
        result = await desktop.get_screen_info()
        print(f"Screen info: {result}")
        
        # Test typing (be careful with this)
        print("⌨️ Testing typing (will type 'Hello Desktop!')...")
        await asyncio.sleep(2)  # Give time to focus somewhere safe
        result = await desktop.type_text("Hello Desktop!")
        print(f"Typing result: {result}")
        
        print("✅ Desktop automation tests completed successfully!")
        
    except Exception as e:
        print(f"❌ Desktop automation test failed: {e}")

async def test_unified_automation():
    """Test unified automation system"""
    print("🔄 Testing Unified Automation...")
    
    config = Config()
    unified = UnifiedAutomation(driver=None, config=config)
    
    try:
        # Test desktop task
        desktop_task = {
            'type': 'desktop',
            'action': 'screenshot',
            'params': {
                'filename': 'test_screenshot.png'
            }
        }
        
        print("📸 Executing desktop screenshot task...")
        result = await unified.execute_task(desktop_task)
        print(f"Desktop task result: {result}")
        
        # Test mouse position task
        mouse_task = {
            'type': 'desktop',
            'action': 'get_mouse_position',
            'params': {}
        }
        
        print("🖱️ Executing mouse position task...")
        result = await unified.execute_task(mouse_task)
        print(f"Mouse position task result: {result}")
        
        # Test application opening
        app_task = {
            'type': 'desktop',
            'action': 'open_app',
            'params': {
                'app_name': 'Calculator'
            }
        }
        
        print("🧮 Executing open Calculator task...")
        result = await unified.execute_task(app_task)
        print(f"Open app task result: {result}")
        
        print("✅ Unified automation tests completed successfully!")
        
    except Exception as e:
        print(f"❌ Unified automation test failed: {e}")

async def test_task_sequence():
    """Test a sequence of tasks"""
    print("📋 Testing Task Sequence...")
    
    config = Config()
    unified = UnifiedAutomation(driver=None, config=config)
    
    tasks = [
        {
            'type': 'desktop',
            'action': 'screenshot',
            'params': {'filename': 'before_calc.png'}
        },
        {
            'type': 'desktop',
            'action': 'open_app',
            'params': {'app_name': 'Calculator'}
        },
        {
            'type': 'desktop',
            'action': 'get_mouse_position',
            'params': {}
        }
    ]
    
    try:
        print("🔄 Executing task sequence...")
        results = await unified.execute_sequence(tasks)
        
        for i, result in enumerate(results):
            print(f"Task {i+1} result: {result}")
        
        print("✅ Task sequence completed successfully!")
        
    except Exception as e:
        print(f"❌ Task sequence test failed: {e}")

def test_imports():
    """Test that all imports work correctly"""
    print("📦 Testing imports...")
    
    try:
        # Test PyAutoGUI import
        import pyautogui
        print(f"✅ PyAutoGUI version: {pyautogui.__version__}")
        
        # Test OpenCV import
        import cv2
        print(f"✅ OpenCV version: {cv2.__version__}")
        
        # Test PIL import
        from PIL import Image
        print("✅ PIL/Pillow imported successfully")
        
        # Test our modules
        from brouser_agent.utils.desktop_automation import DesktopAutomation
        from brouser_agent.utils.unified_automation import UnifiedAutomation
        print("✅ Custom automation modules imported successfully")
        
        print("✅ All imports successful!")
        return True
        
    except ImportError as e:
        print(f"❌ Import failed: {e}")
        return False

async def main():
    """Main test function"""
    print("🚀 Starting Unified Automation Tests")
    print("=" * 50)
    
    # Test imports first
    if not test_imports():
        print("❌ Import tests failed. Please install missing dependencies.")
        return
    
    print("\n" + "=" * 50)
    
    # Test desktop automation
    await test_desktop_automation()
    
    print("\n" + "=" * 50)
    
    # Test unified automation
    await test_unified_automation()
    
    print("\n" + "=" * 50)
    
    # Test task sequence
    await test_task_sequence()
    
    print("\n" + "=" * 50)
    print("🎉 All tests completed!")
    print("\nNote: Some tests may have opened applications or taken screenshots.")
    print("Check your desktop and the project directory for any generated files.")

if __name__ == "__main__":
    # Run the tests
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n⏹️ Tests interrupted by user")
    except Exception as e:
        print(f"\n❌ Test execution failed: {e}")
        import traceback
        traceback.print_exc()