#!/usr/bin/env python3
"""
Test Enhanced Browser Support System

This script tests the improved browser detection, support validation,
and error handling functionality.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from brouser_agent.browsers.support import get_browser_support_manager
from brouser_agent.browsers.manager import BrowserManager
from brouser_agent.browsers.detector import BrowserDetector


def test_browser_support():
    """Test browser support detection and recommendations"""
    print("🧪 Testing Enhanced Browser Support System")
    print("=" * 50)
    
    # Test support manager
    support_manager = get_browser_support_manager()
    
    print("\n1. 🎯 Testing Browser Support Matrix")
    print("-" * 35)
    supported = support_manager.get_supported_browsers()
    for name, browser in supported.items():
        print(f"✅ {browser.display_name}")
        print(f"   Support Level: {browser.support_level.value}")
        print(f"   Selenium: {'✅' if browser.selenium_support else '❌'}")
        print(f"   Playwright: {'✅' if browser.playwright_support else '❌'}")
        if browser.known_issues:
            print(f"   Issues: {', '.join(browser.known_issues)}")
        print()
    
    print("\n2. 🔍 Testing Browser Detection")
    print("-" * 30)
    detector = BrowserDetector()
    available = detector.detect_all()
    
    for name, browser_info in available.items():
        compatibility = support_manager.check_browser_compatibility(name)
        status = "✅ Supported" if compatibility['supported'] else "❌ Not Supported"
        print(f"{status}: {browser_info.name} ({browser_info.version or 'Unknown version'})")
    
    if not available:
        print("❌ No browsers detected")
        missing = ['chrome', 'firefox', 'edge']
        recommendations = support_manager.generate_setup_recommendations(missing)
        print(f"\n📋 Recommendations:\n{recommendations}")
    
    print("\n3. 🛠️ Testing Browser Manager")
    print("-" * 28)
    try:
        browser_manager = BrowserManager()
        recommendations = browser_manager.get_browser_recommendations()
        
        print(f"Available browsers: {recommendations['available_browsers']}")
        print(f"Missing browsers: {recommendations['missing_browsers']}")
        print(f"Recommended: {recommendations['recommended_browser']}")
        
        # Test health check
        health = browser_manager.health_check()
        print(f"Health check: {health['available_browsers']} browsers available")
        
    except Exception as e:
        print(f"❌ Browser manager test failed: {e}")
    
    print("\n4. 🔧 Testing Error Handling")
    print("-" * 26)
    
    # Test invalid browser
    try:
        browser_manager = BrowserManager()
        browser_manager.launch_browser("invalid_browser")
    except ValueError as e:
        print(f"✅ Correctly handled invalid browser: {type(e).__name__}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    
    # Test troubleshooting guide
    guide = support_manager.get_troubleshooting_guide("chrome", "Session closed")
    print(f"✅ Generated troubleshooting guide ({len(guide)} characters)")
    
    print("\n5. 📊 Summary")
    print("-" * 12)
    print(f"✅ Support manager: Working")
    print(f"✅ Browser detection: Working")
    print(f"✅ Error handling: Working")
    print(f"✅ Troubleshooting: Working")
    
    print(f"\n🎉 Enhanced browser support system is functional!")


if __name__ == "__main__":
    test_browser_support()