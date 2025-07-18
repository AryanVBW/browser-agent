#!/usr/bin/env python3
"""
Quick Fix for Browser Agent Dependencies

This script fixes common dependency issues and gets the system running.
"""

import sys
import subprocess

def main():
    print("🔧 Browser Agent Quick Fix")
    print("=" * 30)
    
    print("\n1. 📦 Installing core dependencies...")
    
    # Install core packages one by one to identify issues
    core_packages = [
        "customtkinter>=5.2.0",
        "selenium>=4.15.0", 
        "webdriver-manager>=4.0.0",
        "beautifulsoup4>=4.12.0",
        "requests>=2.31.0",
        "python-dotenv>=1.0.0",
        "psutil>=5.9.0",
        "colorama>=0.4.0",
        "pillow>=10.0.0"
    ]
    
    for package in core_packages:
        try:
            print(f"   Installing {package}...")
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", package
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"   ✅ {package}")
        except subprocess.CalledProcessError:
            print(f"   ⚠️  {package} - trying alternative...")
            try:
                # Try without version constraint
                base_package = package.split(">=")[0]
                subprocess.check_call([
                    sys.executable, "-m", "pip", "install", base_package
                ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                print(f"   ✅ {base_package} (fallback)")
            except:
                print(f"   ❌ {package} failed")
    
    print("\n2. 🤖 Installing AI packages...")
    
    ai_packages = [
        "openai>=1.3.0",
        "anthropic>=0.7.0", 
        "google-generativeai>=0.3.0"
    ]
    
    for package in ai_packages:
        try:
            print(f"   Installing {package}...")
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", package
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"   ✅ {package}")
        except subprocess.CalledProcessError:
            print(f"   ⚠️  {package} - optional, can configure later")
    
    print("\n3. 🎭 Installing browser automation (optional)...")
    
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "playwright>=1.40.0"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("   ✅ Playwright installed")
    except:
        print("   ⚠️  Playwright optional - Selenium will be used")
    
    print("\n4. 🧪 Testing installation...")
    
    # Test critical imports
    try:
        import customtkinter
        print("   ✅ GUI framework")
    except ImportError:
        print("   ❌ GUI framework - install customtkinter manually")
        return 1
    
    try:
        import selenium
        print("   ✅ Browser automation")
    except ImportError:
        print("   ❌ Browser automation - install selenium manually") 
        return 1
    
    print("\n🎉 Quick fix complete!")
    print("\nNext steps:")
    print("1. python test_install.py  # Verify installation")
    print("2. python run_gui.py       # Launch GUI")
    
    return 0

if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n👋 Quick fix cancelled")
        sys.exit(0)