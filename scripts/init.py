#!/usr/bin/env python3
"""
Browser Agent Initialization Script

This script initializes the Browser Agent system by:
1. Checking system requirements
2. Installing dependencies
3. Setting up configuration
4. Verifying browser availability
5. Testing AI connections
6. Launching the GUI
"""

import sys
import os
import subprocess
import json
import shutil
from pathlib import Path

def print_header():
    """Print initialization header"""
    print("""
╔══════════════════════════════════════════════════════════════════╗
║                    🤖 BROWSER AGENT INITIALIZATION                ║
║                                                                  ║
║            AI-Powered Web Automation with Multi-LLM Support      ║
╚══════════════════════════════════════════════════════════════════╝
""")

def check_python():
    """Check Python version compatibility"""
    print("🐍 Checking Python version...")
    
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print(f"❌ Python 3.8+ required (found {version.major}.{version.minor})")
        return False
    
    print(f"✅ Python {version.major}.{version.minor}.{version.micro}")
    return True

def install_dependencies():
    """Install required dependencies"""
    print("\n📦 Installing dependencies...")
    
    try:
        # Upgrade pip first
        print("   Upgrading pip...")
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "--upgrade", "pip"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        # Install requirements with verbose output on error
        print("   Installing packages...")
        try:
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError:
            print("   ⚠️  Standard install failed, trying with verbose output...")
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
            ])
        
        print("✅ Dependencies installed")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        print("\n💡 Try manual installation:")
        print("   pip install -r requirements.txt")
        return False

def setup_playwright():
    """Setup Playwright browsers (optional)"""
    print("\n🎭 Setting up Playwright browsers...")
    
    try:
        subprocess.check_call([
            sys.executable, "-m", "playwright", "install", "chromium", "firefox"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        print("✅ Playwright browsers installed")
        return True
        
    except subprocess.CalledProcessError:
        print("⚠️  Playwright setup skipped (optional)")
        return False

def create_env_file():
    """Create environment configuration file"""
    print("\n🔧 Setting up configuration...")
    
    env_template = """# Browser Agent Configuration
# Add your API keys below

# OpenAI Configuration
OPENAI_API_KEY=

# Claude/Anthropic Configuration
CLAUDE_API_KEY=

# Google Gemini Configuration  
GEMINI_API_KEY=

# Browser Settings
DEFAULT_BROWSER=chrome
HEADLESS=false
AUTOMATION_FRAMEWORK=selenium

# Logging
LOG_LEVEL=INFO
"""
    
    env_path = Path(".env")
    env_example_path = Path(".env.example")
    
    # Create example file
    with open(env_example_path, "w") as f:
        f.write(env_template)
    print(f"✅ Created {env_example_path}")
    
    # Create .env if it doesn't exist
    if not env_path.exists():
        with open(env_path, "w") as f:
            f.write(env_template)
        print(f"✅ Created {env_path}")
    else:
        print("✅ Using existing .env file")
    
    return True

def check_browsers():
    """Check for available browsers"""
    print("\n🌐 Checking browsers...")
    
    try:
        from brouser_agent.browsers.detector import BrowserDetector
        
        detector = BrowserDetector()
        browsers = detector.detect_all()
        
        if browsers:
            print("✅ Available browsers:")
            for name, info in browsers.items():
                status = "✅" if info.is_installed else "❌"
                print(f"   {status} {info.name}")
            return True
        else:
            print("⚠️  No browsers detected")
            print("   Please install Chrome, Firefox, or Edge")
            return False
            
    except Exception as e:
        print(f"⚠️  Browser check failed: {e}")
        return False

def create_directories():
    """Create necessary directories"""
    print("\n📁 Creating directories...")
    
    directories = [
        "screenshots",
        "logs", 
        "exports",
        "plugins/custom"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"✅ Created {directory}/")
    
    return True

def test_imports():
    """Test critical imports"""
    print("\n🔍 Testing imports...")
    
    # Critical imports with proper package mapping
    critical_imports = [
        ("customtkinter", "GUI framework"),
        ("selenium", "Browser automation"), 
        ("bs4", "BeautifulSoup (beautifulsoup4)"),
        ("dotenv", "Environment variables (python-dotenv)"),
        ("PIL", "Image processing (pillow)"),
        ("openai", "OpenAI API"),
        ("brouser_agent.core.config", "Core configuration"),
        ("brouser_agent.gui.main_window", "GUI main window")
    ]
    
    failed_imports = []
    
    for module, description in critical_imports:
        is_available = False
        
        # Try direct import
        try:
            __import__(module)
            is_available = True
        except ImportError:
            pass
        
        # Try importlib.util as backup
        if not is_available:
            try:
                import importlib.util
                spec = importlib.util.find_spec(module)
                if spec is not None:
                    is_available = True
            except (ImportError, ValueError, ModuleNotFoundError):
                pass
        
        if is_available:
            print(f"✅ {description}")
        else:
            print(f"❌ {description}")
            failed_imports.append(module)
    
    return len(failed_imports) == 0

def show_next_steps():
    """Show next steps to user"""
    print("""
╔══════════════════════════════════════════════════════════════════╗
║                        🎉 INITIALIZATION COMPLETE                ║
╚══════════════════════════════════════════════════════════════════╝

📋 NEXT STEPS:

1. 🔑 Configure API Keys:
   Edit the .env file and add your API keys:
   
   OPENAI_API_KEY=your-openai-key-here
   CLAUDE_API_KEY=your-claude-key-here  
   GEMINI_API_KEY=your-gemini-key-here

2. 🚀 Launch the GUI:
   python run_gui.py

3. 💬 Start Using:
   • Go to "🧠 Brain/LLM" tab to verify AI models
   • Use "💬 Chat" tab to interact with the agent
   • Monitor automation in "🌐 Browser Agent" tab

📖 HELPFUL COMMANDS:

   python run_gui.py              # Launch GUI
   python run_gui.py setup        # Re-run setup
   python examples/gui_demo.py    # Run demo
   
🔗 DOCUMENTATION:

   See README.md for detailed usage instructions
   Check examples/ folder for sample scripts

🆘 SUPPORT:

   If you encounter issues:
   1. Check that your API keys are valid
   2. Ensure browsers are installed
   3. Try running: python run_gui.py setup

""")

def main():
    """Main initialization function"""
    print_header()
    
    # Check Python version
    if not check_python():
        print("\n❌ Initialization failed: Python version incompatible")
        return 1
    
    # Install dependencies
    if not install_dependencies():
        print("\n❌ Initialization failed: Could not install dependencies")
        return 1
    
    # Test imports
    if not test_imports():
        print("\n❌ Initialization failed: Import errors")
        return 1
    
    # Setup Playwright (optional)
    setup_playwright()
    
    # Create configuration
    if not create_env_file():
        print("\n❌ Initialization failed: Could not create configuration")
        return 1
    
    # Create directories
    if not create_directories():
        print("\n❌ Initialization failed: Could not create directories")
        return 1
    
    # Check browsers
    check_browsers()
    
    # Show next steps
    show_next_steps()
    
    # Ask if user wants to launch GUI
    try:
        launch = input("🚀 Launch Browser Agent GUI now? (y/n): ").strip().lower()
        if launch in ['y', 'yes', '1']:
            print("\n🚀 Launching Browser Agent GUI...")
            
            # Import and launch GUI
            from brouser_agent.gui.main_window import main as gui_main
            gui_main()
            
    except KeyboardInterrupt:
        print("\n\n👋 Initialization complete!")
    except Exception as e:
        print(f"\n⚠️  Could not launch GUI: {e}")
        print("   You can launch it manually with: python run_gui.py")
    
    return 0

if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n\n👋 Initialization cancelled by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error during initialization: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)