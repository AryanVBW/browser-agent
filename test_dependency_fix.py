#!/usr/bin/env python3
"""
Test script to validate the dependency detection fix

This script verifies that the fixed dependency detection logic correctly
identifies installed packages without false negatives.
"""

import sys
import os
import subprocess
import importlib.util
import pkg_resources

def print_header():
    """Print test header"""
    print("🧪 Testing Dependency Detection Fix")
    print("=" * 40)
    print(f"🐍 Python: {sys.version}")
    print(f"📍 Executable: {sys.executable}")
    print()

def test_problematic_packages():
    """Test the specific packages that were showing false negatives"""
    print("🔍 Testing Previously Problematic Packages:")
    print("-" * 45)
    
    problematic_packages = {
        'beautifulsoup4': 'bs4',
        'google-generativeai': 'google.generativeai',
        'python-dotenv': 'dotenv', 
        'pillow': 'PIL'
    }
    
    for pypi_name, import_name in problematic_packages.items():
        print(f"\n📦 Testing {pypi_name} -> {import_name}")
        
        # Test Method 1: Direct import
        try:
            __import__(import_name)
            method1 = "✅"
        except ImportError:
            method1 = "❌"
        
        # Test Method 2: pkg_resources
        try:
            pkg_resources.get_distribution(pypi_name)
            method2 = "✅"
        except pkg_resources.DistributionNotFound:
            method2 = "❌"
        except Exception:
            method2 = "❌"
        
        # Test Method 3: importlib.util
        try:
            spec = importlib.util.find_spec(import_name)
            method3 = "✅" if spec is not None else "❌"
        except (ImportError, ValueError, ModuleNotFoundError):
            method3 = "❌"
        
        print(f"   Direct import:    {method1}")
        print(f"   pkg_resources:    {method2}")
        print(f"   importlib.util:   {method3}")
        
        # Overall assessment
        if method1 == "✅" or method2 == "✅":
            print(f"   🎯 RESULT:        ✅ CORRECTLY DETECTED")
        else:
            print(f"   🎯 RESULT:        ❌ DETECTION FAILED")

def test_fixed_detection_function():
    """Test the fixed detection function"""
    print("\n🔧 Testing Fixed Detection Function:")
    print("-" * 35)
    
    # Copy of the fixed function from run_gui.py
    package_mapping = {
        'customtkinter': 'customtkinter',
        'selenium': 'selenium',
        'webdriver-manager': 'webdriver_manager',
        'playwright': 'playwright', 
        'beautifulsoup4': 'bs4',
        'requests': 'requests',
        'openai': 'openai',
        'anthropic': 'anthropic',
        'google-generativeai': 'google.generativeai',
        'python-dotenv': 'dotenv',
        'schedule': 'schedule',
        'psutil': 'psutil',
        'colorama': 'colorama',
        'pydantic': 'pydantic',
        'pillow': 'PIL'
    }
    
    detected_packages = []
    missing_packages = []
    
    for pypi_name, import_name in package_mapping.items():
        is_installed = False
        
        # Method 1: Try direct import
        try:
            __import__(import_name)
            is_installed = True
        except ImportError:
            pass
        
        # Method 2: Try pkg_resources if import failed
        if not is_installed:
            try:
                pkg_resources.get_distribution(pypi_name)
                is_installed = True
            except (pkg_resources.DistributionNotFound, ImportError):
                pass
            except Exception:
                pass
        
        # Method 3: Try importlib.util as final check
        if not is_installed:
            try:
                spec = importlib.util.find_spec(import_name)
                if spec is not None:
                    is_installed = True
            except (ImportError, ValueError, ModuleNotFoundError):
                pass
        
        if is_installed:
            print(f"✅ {pypi_name}")
            detected_packages.append(pypi_name)
        else:
            print(f"❌ {pypi_name}")
            missing_packages.append(pypi_name)
    
    return detected_packages, missing_packages

def verify_with_pip():
    """Verify package installation using pip list"""
    print("\n🔍 Cross-checking with pip list:")
    print("-" * 30)
    
    try:
        result = subprocess.run([
            sys.executable, "-m", "pip", "list", "--format=freeze"
        ], capture_output=True, text=True, check=True)
        
        installed_packages = set()
        for line in result.stdout.strip().split('\n'):
            if '==' in line:
                package_name = line.split('==')[0].lower()
                installed_packages.add(package_name)
        
        # Check problematic packages
        problematic = ['beautifulsoup4', 'google-generativeai', 'python-dotenv', 'pillow']
        
        for package in problematic:
            if package.lower() in installed_packages:
                print(f"✅ {package} (confirmed by pip)")
            else:
                print(f"❌ {package} (not in pip list)")
                
        return installed_packages
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running pip list: {e}")
        return set()

def main():
    """Main test function"""
    print_header()
    
    # Test problematic packages
    test_problematic_packages()
    
    # Test fixed detection function
    detected, missing = test_fixed_detection_function()
    
    # Verify with pip
    pip_packages = verify_with_pip()
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 SUMMARY:")
    print(f"   Packages detected: {len(detected)}")
    print(f"   Packages missing:  {len(missing)}")
    
    if missing:
        print(f"   Missing packages:  {', '.join(missing)}")
    
    # Test the specific problematic packages
    problematic_fixed = True
    problematic_packages = ['beautifulsoup4', 'google-generativeai', 'python-dotenv', 'pillow']
    
    for package in problematic_packages:
        if package in missing:
            print(f"   ⚠️  {package} still showing as missing")
            problematic_fixed = False
    
    if problematic_fixed:
        print("\n🎉 SUCCESS: All previously problematic packages are now correctly detected!")
    else:
        print("\n❌ ISSUE: Some packages still showing false negatives")
    
    print("\n🔧 The dependency detection logic has been fixed in:")
    print("   - run_gui.py")
    print("   - init.py")
    print("\n📋 Next steps:")
    print("   1. Run: python run_gui.py")
    print("   2. Verify all packages show as ✅")

if __name__ == "__main__":
    main()