#!/usr/bin/env python3
"""
Fix dependency detection for Browser Agent setup

This script identifies and fixes the package detection issues.
"""

import sys
import importlib.util
import pkg_resources
from typing import Dict, List, Tuple

def test_package_detection():
    """Test different methods of package detection"""
    
    # Define the package mapping (PyPI name -> import name)
    package_mapping = {
        'beautifulsoup4': 'bs4',
        'google-generativeai': 'google.generativeai', 
        'python-dotenv': 'dotenv',
        'pillow': 'PIL',
        'customtkinter': 'customtkinter',
        'selenium': 'selenium',
        'webdriver-manager': 'webdriver_manager',
        'playwright': 'playwright',
        'requests': 'requests',
        'openai': 'openai',
        'anthropic': 'anthropic',
        'schedule': 'schedule',
        'psutil': 'psutil',
        'colorama': 'colorama',
        'pydantic': 'pydantic',
        'aiofiles': 'aiofiles'
    }
    
    print("🔍 Testing Package Detection Methods")
    print("=" * 50)
    
    for pypi_name, import_name in package_mapping.items():
        print(f"\n📦 Testing: {pypi_name} -> {import_name}")
        
        # Method 1: Direct import
        try:
            __import__(import_name)
            method1_result = "✅"
        except ImportError:
            method1_result = "❌"
        
        # Method 2: importlib.util.find_spec
        try:
            spec = importlib.util.find_spec(import_name)
            method2_result = "✅" if spec is not None else "❌"
        except (ImportError, ValueError, ModuleNotFoundError):
            method2_result = "❌"
        
        # Method 3: pkg_resources
        try:
            pkg_resources.get_distribution(pypi_name)
            method3_result = "✅"
        except pkg_resources.DistributionNotFound:
            method3_result = "❌"
        except Exception:
            method3_result = "❌"
        
        print(f"   Direct import:     {method1_result}")
        print(f"   importlib.util:    {method2_result}")
        print(f"   pkg_resources:     {method3_result}")
        
        # Overall result
        if method1_result == "✅" or method3_result == "✅":
            print(f"   📊 Overall:        ✅ INSTALLED")
        else:
            print(f"   📊 Overall:        ❌ MISSING")

def improved_check_dependencies() -> Tuple[bool, List[str]]:
    """Improved dependency checking function"""
    
    # Package mapping: PyPI name -> import name
    package_mapping = {
        'customtkinter': 'customtkinter',
        'selenium': 'selenium',
        'webdriver-manager': 'webdriver_manager',
        'playwright': 'playwright',
        'beautifulsoup4': 'bs4',
        'requests': 'requests',
        'openai': 'openai',
        'python-dotenv': 'dotenv',
        'schedule': 'schedule',
        'psutil': 'psutil',
        'colorama': 'colorama',
        'pydantic': 'pydantic',
        'pillow': 'PIL',
        'google-generativeai': 'google.generativeai',
        'anthropic': 'anthropic',
        'aiofiles': 'aiofiles'
    }
    
    print("📦 Checking dependencies with improved detection...")
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
            except pkg_resources.DistributionNotFound:
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
        else:
            print(f"❌ {pypi_name}")
            missing_packages.append(pypi_name)
    
    return len(missing_packages) == 0, missing_packages

def main():
    """Main testing function"""
    print("🔧 Browser Agent Dependency Detection Fix")
    print("=" * 45)
    
    print(f"🐍 Python: {sys.version}")
    print(f"📍 Executable: {sys.executable}")
    
    # Test current detection method
    print("\n" + "=" * 50)
    test_package_detection()
    
    # Test improved detection
    print("\n" + "=" * 50)
    all_installed, missing = improved_check_dependencies()
    
    print(f"\n📊 SUMMARY:")
    print(f"All packages installed: {all_installed}")
    if missing:
        print(f"Missing packages: {missing}")
    else:
        print("🎉 All packages detected correctly!")

if __name__ == "__main__":
    main()