# 🤖 Browser Agent - AI-Powered Web Automation

<div align="center">

![Browser Agent Logo](img/Brouser_agent.png)

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GUI](https://img.shields.io/badge/Interface-GUI-green.svg)](#gui-interface)
[![Multi-LLM](https://img.shields.io/badge/AI-Multi--LLM-purple.svg)](#multi-llm-support)

*A powerful Python-based AI agent with a modern GUI that intelligently automates web browsers using natural language commands. Features multi-LLM support (OpenAI, Claude, Gemini) and an intuitive graphical interface.*

[🚀 Quick Start](#quick-start) • [📖 Documentation](#documentation) • [🖼️ Screenshots](#screenshots) • [🔧 Features](#features)

</div>

---

## 📖 Table of Contents

- [🎯 Overview](#overview)
- [✨ Features](#features)
- [🖼️ Screenshots](#screenshots)
- [🚀 Quick Start](#quick-start)
- [📱 GUI Interface Guide](#gui-interface-guide)
- [🔧 Configuration](#configuration)
- [💡 Usage Examples](#usage-examples)
- [🔌 Plugin System](#plugin-system)
- [🛠️ Troubleshooting](#troubleshooting)
- [🤝 Contributing](#contributing)

---

## 🎯 Overview

Browser Agent is a next-generation web automation tool that combines the power of artificial intelligence with intuitive browser control. Instead of writing complex scripts, simply tell the AI what you want to accomplish in plain English, and watch as it intelligently navigates websites, fills forms, extracts data, and performs complex web tasks.

### 🌟 What Makes It Special?

- **🧠 Multi-AI Brain**: Supports OpenAI GPT, Claude, and Gemini models
- **🎨 Modern GUI**: Beautiful, responsive interface with real-time feedback  
- **🤖 Natural Language**: Control browsers using conversational commands
- **🔄 Smart Automation**: Human-like interaction patterns with error recovery
- **📊 Complete Monitoring**: Real-time logs, task history, and performance metrics

---

## ✨ Features

### 🖥️ **Modern GUI Interface**
- **Intuitive Design**: Clean, modern interface with dark/light themes
- **Animated Chat**: Real-time conversations with typing animations
- **Tabbed Layout**: Organized sections for different functionalities
- **Visual Feedback**: Progress bars, status indicators, and live updates
- **Cross-Platform**: Works seamlessly on Windows, macOS, and Linux

### 🧠 **Multi-LLM Brain System**
- **OpenAI Integration**: GPT-3.5, GPT-4, and GPT-4 Turbo support
- **Claude Integration**: Opus, Sonnet, and Haiku models from Anthropic
- **Gemini Integration**: Google's Pro and Pro Vision models
- **Dynamic Switching**: Change AI models on-the-fly during conversations
- **Performance Metrics**: Track response times, costs, and success rates

### 🌐 **Advanced Browser Automation**
- **Multi-Browser Support**: Chrome, Firefox, Edge, Safari auto-detection
- **Dual Framework**: Both Selenium and Playwright support
- **Human-like Behavior**: Realistic delays and natural interaction patterns
- **Smart Recovery**: Intelligent error handling with retry logic
- **Live Monitoring**: Real-time automation logs and screenshots
- **Manual Override**: Direct browser control when needed

### 📊 **Comprehensive Management**
- **Task History**: Complete execution logs with filtering and search
- **Settings Control**: Extensive configuration options
- **Plugin Architecture**: Extensible system for specialized tasks
- **Security Features**: Container support and secure execution
- **Performance Monitoring**: Real-time resource usage tracking

---

## 🖼️ Screenshots

### 💬 Chat Interface - Natural Language Interaction
![Chat Interface](img/chat.png)
*Chat with the AI using natural language to control browsers and automate web tasks. Features animated responses, quick actions, and real-time status updates.*

### 🧠 Brain/LLM Configuration - AI Model Management  
![Brain LLM Tab](img/Brain:LLM.png)
*Configure multiple AI providers, manage API keys, select models, and monitor performance metrics. Switch between OpenAI, Claude, and Gemini models seamlessly.*

### 📋 Task Log - Complete History & Analytics
![Task Log](img/tasklog.png)
*Track all executed tasks with detailed logs, success rates, and performance metrics. Filter, search, and export task history for analysis.*

### ⚙️ Settings - Comprehensive Configuration
![Settings](img/settings.png)
*Customize every aspect of the browser agent including automation behavior, security settings, performance tuning, and browser preferences.*

---

## 🚀 Quick Start

### 📋 Prerequisites

- **Python 3.8+** (3.12+ recommended)
- **Modern Browser** (Chrome, Firefox, Edge, or Safari)
- **Internet Connection** (for AI API access)

### ⚡ One-Command Installation

```bash
# Clone the repository
git clone https://github.com/your-username/brouser-agent.git
cd brouser-agent

# Automatic setup (installs dependencies and checks environment)
python run_gui.py setup

# Launch the GUI
python run_gui.py
```

### 🔑 API Configuration

1. **Get API Keys** from one or more providers:
   - [OpenAI API Key](https://platform.openai.com/api-keys)
   - [Claude API Key](https://console.anthropic.com/)
   - [Gemini API Key](https://makersuite.google.com/app/apikey)

2. **Configure in GUI**:
   - Launch the application: `python run_gui.py`
   - Go to the "🧠 Brain/LLM" tab
   - Enter your API keys and test connectivity

3. **Or use Environment Variables**:
   ```bash
   export OPENAI_API_KEY="your-openai-api-key"
   export CLAUDE_API_KEY="your-claude-api-key" 
   export GEMINI_API_KEY="your-gemini-api-key"
   ```

### 🎯 First Steps

1. **Launch GUI**: `python run_gui.py`
2. **Configure AI**: Add API keys in the "🧠 Brain/LLM" tab
3. **Start Chatting**: Go to "💬 Chat" tab and try: *"Search Google for Python tutorials"*
4. **Monitor Progress**: Watch live automation in "🌐 Browser Agent" tab
5. **Check History**: View completed tasks in "📜 Task Log" tab

---

## 📱 GUI Interface Guide

### 💬 **Chat Tab - Main Interaction Hub**

The chat interface is your primary way to interact with the AI agent:

- **Natural Commands**: Type requests like *"Go to Amazon and find wireless headphones under $50"*
- **Animated Responses**: Watch AI responses appear with realistic typing effects
- **Quick Actions**: Pre-built buttons for common tasks (Search Google, Check Email, etc.)
- **Status Indicators**: Real-time feedback showing when AI is thinking or executing
- **Chat History**: Scroll through previous conversations and responses

**Example Commands:**
```
"Search YouTube for Python programming tutorials"
"Go to Amazon, search for laptop, and add the first result to cart"
"Fill out the contact form with my information"
"Navigate to news.ycombinator.com and extract top story titles"
```

### 🧠 **Brain/LLM Tab - AI Configuration Center**

Configure and manage your AI models:

- **Provider Selection**: Choose between OpenAI, Claude, and Gemini
- **Model Selection**: Pick specific models (GPT-4, Claude Opus, Gemini Pro, etc.)
- **API Key Management**: Securely store and test API credentials
- **Performance Metrics**: Monitor response times, token usage, and costs
- **Model Testing**: Test AI responses before using in automation
- **Advanced Settings**: Temperature, max tokens, and model-specific options

### 🌐 **Browser Agent Tab - Automation Control**

Monitor and control browser automation:

- **Browser Detection**: Automatically discovers installed browsers
- **Live Control Panel**: Launch, close, and manage browser instances
- **Automation Logs**: Real-time feed of all browser actions and decisions
- **Manual Override**: Direct browser control for testing and debugging
- **Screenshot Capture**: Automatic screenshots during task execution
- **Performance Stats**: Execution times and success rates

### 📜 **Task Log Tab - History & Analytics**

Complete task management and analysis:

- **Execution History**: Every task with timestamps, prompts, and results
- **Advanced Filtering**: Filter by date, status, success rate, or AI model
- **Search Functionality**: Find specific tasks using keywords
- **Export Options**: Save history as JSON, CSV, or detailed reports
- **Performance Analytics**: Success rates, average execution times, and trends
- **Task Replay**: Re-run successful tasks or debug failures

### ⚙️ **Settings Tab - System Configuration**

Customize every aspect of the browser agent:

**General Settings:**
- Default browser selection
- Theme preferences (dark/light)
- Logging levels and output formats

**Browser Configuration:**
- Window sizes and positions
- Timeout values and retry attempts
- Headless mode and privacy settings

**Automation Behavior:**
- Human-like delays and interaction patterns
- Scroll speeds and click timings
- Error recovery strategies

**Security & Performance:**
- Permission controls and access restrictions
- Memory limits and resource management
- Container and sandbox options

---

## 🔧 Configuration

### 🌍 Environment Variables

Create a `.env` file or set environment variables:

```bash
# AI Provider API Keys
OPENAI_API_KEY=sk-your-openai-key-here
CLAUDE_API_KEY=sk-ant-your-claude-key-here
GEMINI_API_KEY=your-gemini-api-key-here

# Browser Settings
DEFAULT_BROWSER=chrome
HEADLESS_MODE=false
AUTOMATION_FRAMEWORK=selenium

# Logging
LOG_LEVEL=INFO
LOG_FILE=logs/browser_agent.log
```

### ⚙️ Programmatic Configuration

```python
from brouser_agent import Config, BrowserAgent

# Create custom configuration
config = Config(
    openai_api_key="your-api-key",
    default_browser="chrome",
    headless=False,
    automation_framework="selenium",
    max_retry_attempts=3,
    human_like_delays=True
)

# Initialize agent with config
agent = BrowserAgent(config)
```

### 🎛️ Advanced Settings

```python
# Performance tuning
config.performance.max_memory_mb = 2048
config.performance.max_concurrent_tasks = 3
config.performance.enable_gpu_acceleration = True

# Security settings
config.security.use_container = True
config.security.allow_file_downloads = False
config.security.enable_javascript = True

# Browser behavior
config.browser.window_size = (1920, 1080)
config.browser.page_load_timeout = 30
config.browser.implicit_wait = 10
```

---

## 💡 Usage Examples

### 🛒 **E-commerce Automation**

```python
import asyncio
from brouser_agent import BrowserAgent

async def shop_for_headphones():
    agent = BrowserAgent()
    
    result = await agent.execute_task(
        """Go to Amazon and search for 'wireless noise cancelling headphones'.
        Filter results by price (under $200) and rating (4+ stars).
        Add the top-rated product to cart and proceed to checkout."""
    )
    
    print(f"Shopping task completed: {result.success}")
    print(f"Screenshots saved: {result.screenshots}")

# Run the task
asyncio.run(shop_for_headphones())
```

### 📝 **Form Automation**

```python
async def fill_contact_form():
    agent = BrowserAgent()
    
    # Fill out a contact form with specific information
    await agent.execute_task(
        """Navigate to the contact page and fill out the form:
        - Name: John Smith
        - Email: john.smith@email.com
        - Phone: (555) 123-4567
        - Subject: Product Inquiry
        - Message: I'm interested in learning more about your services.
        
        Review the information and submit the form."""
    )

asyncio.run(fill_contact_form())
```

### 📊 **Data Extraction**

```python
async def extract_news_headlines():
    agent = BrowserAgent()
    
    result = await agent.execute_task(
        """Go to news.ycombinator.com and extract:
        1. Titles of the top 10 stories
        2. Number of points and comments for each
        3. Save the data in a structured format
        
        Take a screenshot of the homepage."""
    )
    
    # Access extracted data
    extracted_data = result.data
    print(f"Found {len(extracted_data['headlines'])} headlines")

asyncio.run(extract_news_headlines())
```

### 🔍 **Research Automation**

```python
async def research_competitors():
    agent = BrowserAgent()
    
    await agent.execute_task(
        """Research competitors for 'project management software':
        
        1. Search Google for 'best project management software 2024'
        2. Visit the top 3 websites from search results
        3. For each site, collect:
           - Pricing information
           - Key features mentioned
           - Customer reviews/ratings
        4. Take screenshots of pricing pages
        5. Compile findings into a summary
        
        Focus on features like team collaboration, time tracking, and integrations."""
    )

asyncio.run(research_competitors())
```

### 📧 **Email & Social Media**

```python
async def check_social_media():
    agent = BrowserAgent()
    
    # Multi-platform social media check
    await agent.execute_task(
        """Check my social media accounts:
        
        1. Go to LinkedIn and check for new messages/connections
        2. Visit Twitter and check mentions and DMs
        3. Check Facebook for notifications
        4. Take screenshots of each platform's main feed
        
        Summarize any important updates or messages."""
    )

asyncio.run(check_social_media())
```

---

## 🔌 Plugin System

Browser Agent features a powerful plugin architecture for extending functionality:

### 🔧 **Built-in Plugins**

- **🛒 E-commerce Plugin**: Shopping cart management, price comparison
- **📝 Form Filler Plugin**: Intelligent form completion with validation
- **📊 Data Extractor Plugin**: Advanced web scraping and data collection
- **📱 Social Media Plugin**: Social platform automation and monitoring
- **📧 Email Plugin**: Email management and automation

### 🚀 **Creating Custom Plugins**

```python
from brouser_agent.plugins.base import BasePlugin, PluginMetadata

class CustomShoppingPlugin(BasePlugin):
    @property
    def metadata(self):
        return PluginMetadata(
            name="custom_shopping",
            version="1.0.0",
            description="Advanced shopping automation",
            author="Your Name",
            tags=["ecommerce", "shopping", "automation"]
        )
    
    def can_handle(self, task_type: str, context: dict) -> bool:
        """Determine if this plugin can handle the task"""
        shopping_keywords = ["buy", "purchase", "shop", "cart", "checkout"]
        return any(keyword in task_type.lower() for keyword in shopping_keywords)
    
    async def execute(self, task_data: dict, browser_session):
        """Execute the custom shopping logic"""
        # Your custom shopping automation logic
        result = await self.perform_shopping_task(task_data, browser_session)
        
        return {
            "success": True,
            "data": result,
            "screenshots": ["shopping_cart.png", "checkout.png"]
        }
    
    async def perform_shopping_task(self, task_data, browser):
        # Implement your shopping logic here
        pass

# Register the plugin
from brouser_agent.plugins.registry import PluginRegistry
registry = PluginRegistry()
registry.register_plugin(CustomShoppingPlugin())
```

### 📦 **Plugin Installation**

```bash
# Install a plugin from file
brouser-agent plugin install ./my_custom_plugin.py

# List installed plugins
brouser-agent plugin list

# Enable/disable plugins
brouser-agent plugin enable custom_shopping
brouser-agent plugin disable form_filler
```

---

## 🛠️ Troubleshooting

### 🚨 **Common Issues & Solutions**

#### **Browser Not Detected**
```bash
# Check available browsers
python -c "from brouser_agent.browsers.detector import BrowserDetector; print(BrowserDetector().detect_browsers())"

# Install Chrome if missing (recommended)
# Windows: Download from google.com/chrome
# macOS: brew install --cask google-chrome
# Linux: sudo apt install google-chrome-stable
```

#### **WebDriver Issues** 
```bash
# Clear WebDriver cache
rm -rf ~/.wdm/

# Force WebDriver update
python -c "from webdriver_manager.chrome import ChromeDriverManager; ChromeDriverManager().install()"
```

#### **API Key Errors**
```bash
# Test API connectivity
python -c "
from brouser_agent.core.multi_llm_processor import MultiLLMProcessor
processor = MultiLLMProcessor()
print(processor.test_api_keys())
"
```

#### **Permission Errors**
```bash
# macOS: Grant Terminal access to control browsers
# Go to System Preferences > Security & Privacy > Privacy > Accessibility

# Linux: Add user to required groups
sudo usermod -a -G audio,video $USER
```

#### **Memory Issues**
```bash
# Reduce memory usage in settings
# Set max_concurrent_tasks = 1
# Enable headless mode
# Reduce screenshot quality
```

### 🔍 **Debug Mode**

Enable detailed logging for troubleshooting:

```bash
# Run with verbose output
python run_gui.py --debug

# Check specific logs
tail -f logs/browser_agent.log
tail -f logs/automation.log
tail -f logs/llm_processor.log
```

### 📋 **System Requirements Check**

```python
# Run system diagnostics
python -c "
from brouser_agent.utils.diagnostics import SystemDiagnostics
diag = SystemDiagnostics()
diag.run_full_check()
"
```

### 🆘 **Getting Help**

1. **Check Logs**: Look in `logs/` directory for detailed error messages
2. **GitHub Issues**: Report bugs at [GitHub Issues](https://github.com/your-username/brouser-agent/issues)
3. **Discussions**: Join community discussions for help and tips
4. **Documentation**: Full API docs available at [documentation link]

---

## 🤝 Contributing

We welcome contributions from the community! Here's how to get started:

### 🔄 **Development Workflow**

```bash
# Fork and clone the repository
git clone https://github.com/your-username/brouser-agent.git
cd brouser-agent

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements-dev.txt
pip install -e .

# Run tests
pytest tests/ -v

# Run linting
flake8 brouser_agent/
black brouser_agent/
isort brouser_agent/

# Create feature branch
git checkout -b feature/amazing-new-feature

# Make changes and commit
git commit -m "Add amazing new feature"
git push origin feature/amazing-new-feature
```

### 🧪 **Testing**

```bash
# Run all tests
pytest

# Run specific test categories
pytest tests/test_browser_automation.py
pytest tests/test_llm_integration.py
pytest tests/test_gui_interface.py

# Run with coverage
pytest --cov=brouser_agent tests/

# Test specific browser
pytest tests/ --browser=chrome
pytest tests/ --browser=firefox
```

### 📝 **Code Standards**

- **Python Style**: Follow PEP 8 and use `black` for formatting
- **Documentation**: Add docstrings to all public methods
- **Type Hints**: Use type annotations for better code clarity
- **Tests**: Write tests for new features and bug fixes
- **Commit Messages**: Use conventional commits (feat:, fix:, docs:, etc.)

### 🎯 **Areas for Contribution**

- **🔌 Plugin Development**: Create specialized automation plugins
- **🌐 Browser Support**: Add support for additional browsers
- **🧠 AI Integration**: Integrate new LLM providers
- **🎨 UI/UX**: Improve the graphical interface
- **📚 Documentation**: Improve docs and examples
- **🧪 Testing**: Expand test coverage
- **🐛 Bug Fixes**: Fix reported issues

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **OpenAI** for GPT models and API
- **Anthropic** for Claude models
- **Google** for Gemini AI models  
- **Selenium** and **Playwright** teams for browser automation frameworks
- **CustomTkinter** for the modern GUI framework
- **Contributors** who make this project better

---

## 🗺️ Roadmap

### 🔮 **Upcoming Features**

- [ ] **Visual AI**: Computer vision for element detection
- [ ] **Multi-Tab Support**: Handle multiple browser tabs simultaneously  
- [ ] **Mobile Browser**: Support for mobile browser automation
- [ ] **Cloud Deployment**: Deploy agents to cloud platforms
- [ ] **Marketplace**: Plugin marketplace and community sharing
- [ ] **Advanced Analytics**: ML-powered performance optimization
- [ ] **Voice Control**: Voice commands for hands-free operation
- [ ] **Collaboration**: Multi-user and team features

### 📊 **Version History**

- **v1.0.0** - Initial release with GUI and multi-LLM support
- **v1.1.0** - Added plugin system and advanced browser automation
- **v1.2.0** - Enhanced GUI with real-time monitoring
- **v1.3.0** - Added task scheduling and performance analytics

---

<div align="center">

## 🚀 Ready to Automate?

**[⬇️ Download Now](https://github.com/your-username/brouser-agent/releases)** • **[📖 Read Docs](#documentation)** • **[🎮 Try Demo](#quick-start)**

---

**Browser Agent** - *Bringing AI-powered automation to web browsing* 🤖✨

Made with ❤️ by the Browser Agent team

[⭐ Star us on GitHub](https://github.com/your-username/brouser-agent) • [🐛 Report Issues](https://github.com/your-username/brouser-agent/issues) • [💬 Join Discussion](https://github.com/your-username/brouser-agent/discussions)

</div>