#!/usr/bin/env python3
"""
Browser Agent GUI Launcher

This script provides a professional launcher for the Browser Agent GUI
with dependency checking, environment setup, and comprehensive error handling.
"""

import sys
import os
import subprocess
import json
import platform
from pathlib import Path
import importlib.util
import argparse

# ASCII Art Banner
BANNER = """
██████╗ ██████╗  ██████╗ ██╗   ██╗███████╗███████╗██████╗      █████╗  ██████╗ ███████╗███╗   ██╗████████╗
██╔══██╗██╔══██╗██╔═══██╗██║   ██║██╔════╝██╔════╝██╔══██╗    ██╔══██╗██╔════╝ ██╔════╝████╗  ██║╚══██╔══╝
██████╔╝██████╔╝██║   ██║██║   ██║███████╗█████╗  ██████╔╝    ███████║██║  ███╗█████╗  ██╔██╗ ██║   ██║   
██╔══██╗██╔══██╗██║   ██║██║   ██║╚════██║██╔══╝  ██╔══██╗    ██╔══██║██║   ██║██╔══╝  ██║╚██╗██║   ██║   
██████╔╝██║  ██║╚██████╔╝╚██████╔╝███████║███████╗██║  ██║    ██║  ██║╚██████╔╝███████╗██║ ╚████║   ██║   
╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝   

🤖 AI-Powered Web Browser Automation with Multi-LLM Support
"""

def print_banner():
    """Print the application banner"""
    print(BANNER)
    print("=" * 100)
    print()

def check_python_version():
    """Check if Python version is compatible"""
    print("🐍 Checking Python version...")
    
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        print(f"   Current version: {sys.version}")
        print("   Please upgrade Python and try again")
        return False
    
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    return True

def check_dependencies():
    """Check if required dependencies are installed"""
    print("\n📦 Checking dependencies...")
    
    # Package mapping: PyPI name -> import name  
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
                import pkg_resources
                pkg_resources.get_distribution(pypi_name)
                is_installed = True
            except (pkg_resources.DistributionNotFound, ImportError):
                pass
            except Exception:
                pass
        
        # Method 3: Try importlib.util as final check
        if not is_installed:
            try:
                import importlib.util
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
    
    if missing_packages:
        print(f"\n❌ Missing packages: {', '.join(missing_packages)}")
        print("   Install with: pip install -r requirements.txt")
        return False
    
    print("✅ All dependencies installed")
    return True

def check_environment():
    """Check environment variables and configuration"""
    print("\n🔑 Checking environment...")
    
    # Check for API keys
    api_keys = {
        'OPENAI_API_KEY': os.getenv('OPENAI_API_KEY'),
        'CLAUDE_API_KEY': os.getenv('CLAUDE_API_KEY'),
        'GEMINI_API_KEY': os.getenv('GEMINI_API_KEY')
    }
    
    configured_providers = []
    for key, value in api_keys.items():
        if value:
            print(f"✅ {key} configured")
            configured_providers.append(key.replace('_API_KEY', ''))
        else:
            print(f"⚠️  {key} not configured")
    
    if not configured_providers:
        print("\n⚠️  No AI provider API keys found!")
        print("   Set at least one of the following environment variables:")
        print("   - OPENAI_API_KEY=your-openai-api-key")
        print("   - CLAUDE_API_KEY=your-claude-api-key")
        print("   - GEMINI_API_KEY=your-gemini-api-key")
        print("\n   You can still run the GUI to configure these in the Brain/LLM tab")
    else:
        print(f"✅ AI providers configured: {', '.join(configured_providers)}")
    
    return True

def check_browsers():
    """Check for installed browsers"""
    print("\n🌐 Checking browsers...")
    
    try:
        # Import browser detector
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        from brouser_agent.browsers.detector import BrowserDetector
        
        detector = BrowserDetector()
        browsers = detector.detect_all()
        
        if browsers:
            print("✅ Available browsers:")
            for name, info in browsers.items():
                status = "✅" if info.is_installed else "❌"
                print(f"   {status} {info.name}")
        else:
            print("⚠️  No browsers detected")
            print("   Please install Chrome, Firefox, or Edge")
            
    except Exception as e:
        print(f"⚠️  Could not check browsers: {e}")
    
    return True

def create_sample_env():
    """Create a sample .env file"""
    env_content = """# Browser Agent Environment Configuration
# Copy this file to .env and add your API keys

# OpenAI Configuration
OPENAI_API_KEY=your-openai-api-key-here

# Claude/Anthropic Configuration  
CLAUDE_API_KEY=your-claude-api-key-here

# Google Gemini Configuration
GEMINI_API_KEY=your-gemini-api-key-here

# Optional: Logging
LOG_LEVEL=INFO
LOG_FILE=browser_agent.log

# Optional: Browser Settings
DEFAULT_BROWSER=chrome
HEADLESS=false
"""
    
    env_path = Path(".env.example")
    if not env_path.exists():
        with open(env_path, "w") as f:
            f.write(env_content)
        print(f"✅ Created {env_path}")

def install_dependencies():
    """Install missing dependencies"""
    print("\n📦 Installing dependencies...")
    
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def setup_playwright():
    """Setup Playwright browsers"""
    print("\n🎭 Setting up Playwright...")
    
    try:
        subprocess.check_call([sys.executable, "-m", "playwright", "install"])
        print("✅ Playwright browsers installed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to setup Playwright: {e}")
        print("   You can skip this and use Selenium instead")
        return False

# Remove the old launch_gui function as it's now integrated into main()

def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description="Browser Agent GUI Launcher",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run_gui.py              # Launch the GUI
  python run_gui.py --setup      # Run initial setup
  python run_gui.py --check      # Check system requirements
  python run_gui.py --version    # Show version information
        """
    )
    
    parser.add_argument(
        "--setup", 
        action="store_true", 
        help="Run initial setup (install dependencies, configure environment)"
    )
    
    parser.add_argument(
        "--check", 
        action="store_true", 
        help="Check system requirements and dependencies"
    )
    
    parser.add_argument(
        "--version", 
        action="store_true", 
        help="Show version information"
    )
    
    parser.add_argument(
        "--verbose", "-v", 
        action="store_true", 
        help="Enable verbose output"
    )
    
    return parser.parse_args()


def show_version():
    """Show version information"""
    try:
        # Try to import version from the package
        sys.path.insert(0, str(Path(__file__).parent))
        from brouser_agent import __version__, __author__
        print(f"Browser Agent v{__version__}")
        print(f"Author: {__author__}")
    except ImportError:
        print("Browser Agent (version unknown - package not installed)")
    
    print(f"Python: {sys.version}")
    print(f"Platform: {platform.platform()}")


def check_system_requirements(verbose=False):
    """Check all system requirements"""
    print("🔍 Checking system requirements...")
    
    all_good = True
    
    # Check Python version
    if verbose:
        print(f"   Python version: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    
    if not check_python_version():
        all_good = False
    else:
        print("   ✅ Python version OK")
    
    # Check dependencies
    if not check_dependencies():
        all_good = False
        print("   ❌ Missing dependencies")
    else:
        print("   ✅ Dependencies OK")
    
    # Check environment
    check_environment()
    
    # Check browsers
    check_browsers()
    
    return all_good


def main():
    """Main launcher function"""
    args = parse_arguments()
    
    print_banner()
    
    # Handle version command
    if args.version:
        show_version()
        return 0
    
    # Handle check command
    if args.check:
        if check_system_requirements(verbose=args.verbose):
            print("\n✅ All system requirements met!")
            return 0
        else:
            print("\n❌ Some requirements not met. Run with --setup to fix.")
            return 1
    
    # Handle setup mode
    if args.setup:
        print("🔧 Running setup mode...")
        
        # Install dependencies
        if not install_dependencies():
            return 1
        
        # Setup Playwright (optional)
        setup_playwright()
        
        # Create sample environment file
        create_sample_env()
        
        print("\n✅ Setup complete!")
        print("   1. Copy .env.example to .env")
        print("   2. Add your API keys to .env")
        print("   3. Run: python run_gui.py")
        return 0
    
    # Check system requirements
    if not check_python_version():
        return 1
    
    # Check dependencies
    if not check_dependencies():
        print("\n🔧 Run 'python run_gui.py --setup' to install dependencies")
        return 1
    
    # Check API keys
    if not check_api_keys():
        print("⚠️  Warning: No API keys configured. Some features may not work.")
        print("   Please configure your API keys in the .env file or GUI settings.")
    
    # Check browsers
    if not check_browsers():
        print("⚠️  Warning: No supported browsers found.")
        print("   Please install Chrome, Firefox, or Edge for full functionality.")
    
    # Launch GUI
    print("\n🚀 Launching Browser Agent GUI...")
    try:
        # Use the professional GUI entry point
        from brouser_agent.gui_main import main as gui_main
        return gui_main()
        
    except ImportError as e:
        print(f"❌ Failed to import GUI module: {e}")
        print("   Please ensure the package is properly installed.")
        print("   Try running: python run_gui.py --setup")
        return 1
        
    except Exception as e:
        print(f"❌ Failed to launch GUI: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1

if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n\n👋 Setup interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)