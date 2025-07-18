#!/usr/bin/env python3
"""
Test installation script for Browser Agent

This script tests if all required dependencies are properly installed.
"""

import sys

def test_imports():
    """Test all critical imports"""
    print("🔍 Testing imports...")
    
    test_cases = [
        ("customtkinter", "Modern GUI framework"),
        ("selenium", "Browser automation"),
        ("webdriver_manager", "WebDriver management"),
        ("playwright", "Alternative browser framework"),
        ("bs4", "BeautifulSoup for HTML parsing"),
        ("requests", "HTTP requests"),
        ("openai", "OpenAI API"),
        ("anthropic", "Claude API"),
        ("google.generativeai", "Gemini API"),
        ("dotenv", "Environment variables"),
        ("schedule", "Task scheduling"),
        ("psutil", "System monitoring"),
        ("colorama", "Colored output"),
        ("pydantic", "Data validation"),
        ("PIL", "Image processing")
    ]
    
    failed_imports = []
    
    for module, description in test_cases:
        try:
            __import__(module)
            print(f"✅ {description}")
        except ImportError as e:
            print(f"❌ {description}: {e}")
            failed_imports.append(module)
    
    return len(failed_imports) == 0, failed_imports

def test_tkinter():
    """Test tkinter availability"""
    print("\n🖼️  Testing GUI framework...")
    
    try:
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()  # Hide the window
        root.destroy()
        print("✅ Tkinter (built-in GUI) works")
        return True
    except Exception as e:
        print(f"❌ Tkinter error: {e}")
        return False

def main():
    """Main test function"""
    print("🧪 Browser Agent Installation Test")
    print("=" * 40)
    
    # Test Python version
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print(f"❌ Python 3.8+ required (found {version.major}.{version.minor})")
        return 1
    
    print(f"✅ Python {version.major}.{version.minor}.{version.micro}")
    
    # Test imports
    imports_ok, failed = test_imports()
    
    # Test GUI
    gui_ok = test_tkinter()
    
    print("\n" + "=" * 40)
    
    if imports_ok and gui_ok:
        print("🎉 All tests passed! Browser Agent is ready to use.")
        print("\nNext steps:")
        print("1. Configure API keys in .env file")
        print("2. Run: python run_gui.py")
        return 0
    else:
        print("❌ Some tests failed.")
        if failed:
            print(f"Missing packages: {', '.join(failed)}")
            print("Run: pip install -r requirements.txt")
        if not gui_ok:
            print("GUI framework issue detected.")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)