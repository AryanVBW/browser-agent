#!/usr/bin/env python3
"""
Browser Agent GUI Launcher

This script provides a complete launcher for the Browser Agent GUI with:
- Dependency checking
- Environment setup
- Configuration validation
- Error handling and recovery
"""

import sys
import os
import subprocess
import json
from pathlib import Path

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

def launch_gui():
    """Launch the Browser Agent GUI"""
    print("\n🚀 Launching Browser Agent GUI...")
    
    try:
        # Add current directory to Python path
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        
        # Import and run the GUI
        from brouser_agent.gui.main_window import main
        main()
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("   Please ensure all dependencies are installed")
        return False
    except Exception as e:
        print(f"❌ Error launching GUI: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Main launcher function"""
    print_banner()
    
    # Check system requirements
    if not check_python_version():
        return 1
    
    # Check if we're in setup mode
    if len(sys.argv) > 1 and sys.argv[1] == "setup":
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
    
    # Check dependencies
    if not check_dependencies():
        print("\n🔧 Run 'python run_gui.py setup' to install dependencies")
        return 1
    
    # Check environment
    check_environment()
    
    # Check browsers
    check_browsers()
    
    # Launch GUI
    if not launch_gui():
        return 1
    
    print("\n👋 Browser Agent GUI closed")
    return 0

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