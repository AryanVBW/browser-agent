# Browser Agent

A powerful, production-ready browser automation platform that combines multi-browser support with AI-driven automation capabilities. Built for developers, QA engineers, and automation enthusiasts who need reliable, scalable web automation solutions.

## 🚀 Features

### Core Capabilities
- **🌐 Multi-Browser Support** - Chrome, Firefox, Safari, and Edge with unified API
- **🤖 AI-Powered Automation** - Intelligent web interaction and task execution
- **🔌 MCP Integration** - Model Context Protocol support for enhanced AI capabilities
- **🖥️ Dual Interface** - Both GUI and CLI for different use cases
- **🧩 Plugin Architecture** - Extensible system with custom plugins
- **☁️ Cloud Ready** - Docker and Kubernetes deployment support
- **🔒 Enterprise Security** - Secure credential management and audit logging

### Platform Support
- ✅ **Windows** (10, 11)
- ✅ **macOS** (10.15+)
- ✅ **Linux** (Ubuntu 18.04+, CentOS 7+)
- ✅ **Docker** containers
- ✅ **Kubernetes** clusters

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)]()
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## 📁 Project Structure

This project follows a production-ready directory structure:

```
brouser-agent/
├── 📂 brouser_agent/           # Main application source code
│   ├── browsers/               # Browser implementations
│   ├── cli/                   # Command-line interface
│   ├── config/                # Configuration management
│   ├── core/                  # Core functionality
│   ├── gui/                   # Graphical user interface
│   ├── mcp/                   # MCP integration
│   ├── plugins/               # Plugin system
│   └── utils/                 # Utility functions
├── 📂 docs/                   # 📚 Documentation
│   ├── README.md              # Documentation overview
│   ├── CONTRIBUTING.md        # Contributor guidelines
│   ├── CHANGELOG.md           # Version history
│   └── *.md                   # Feature & technical docs
├── 📂 tests/                  # 🧪 Test suite
│   ├── README.md              # Testing guidelines
│   ├── pytest.ini            # Test configuration
│   └── test_*.py              # Test files
├── 📂 scripts/                # 🔧 Utility scripts
│   ├── README.md              # Script documentation
│   ├── run_gui.py             # GUI launcher
│   └── *.py                   # Setup & maintenance scripts
├── 📂 config/                 # ⚙️ Configuration files
│   ├── README.md              # Configuration guide
│   ├── .env.example           # Environment template
│   └── *.json                 # App configurations
├── 📂 assets/                 # 🎨 Static assets
│   ├── README.md              # Asset guidelines
│   ├── img/                   # Images and icons
│   └── *.png                  # Screenshots
├── 📂 deployment/             # 🚀 Deployment configs
│   ├── README.md              # Deployment guide
│   ├── Dockerfile             # Container definition
│   └── docker-compose.yml     # Multi-container setup
├── 📂 examples/               # 💡 Example scripts
└── 📂 .github/                # 🔄 GitHub workflows & templates
    ├── ISSUE_TEMPLATE/        # Issue templates
    └── workflows/             # CI/CD pipelines
```

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

### Option 1: Local Installation

```bash
# Clone the repository
git clone https://github.com/your-username/browser-agent.git
cd browser-agent

# Quick setup with make (recommended)
make install
make run

# Or manual setup
pip install -r requirements.txt
python -m brouser_agent
```

### Option 2: Docker (Recommended for Production)

```bash
# Quick start with Docker Compose
docker-compose -f deployment/docker-compose.yml up -d

# Or build and run manually
docker build -f deployment/Dockerfile -t browser-agent .
docker run -p 8080:8080 -e API_KEY="your-key" browser-agent
```

### Option 3: Development Setup

```bash
# Development environment with all tools
make dev-install
make dev-setup
make test

# Start development server
make dev-run
```

## 📚 Documentation

Comprehensive documentation is available in the [`docs/`](docs/) directory:

### 🎯 Getting Started
- **[Installation Guide](docs/installation.md)** - Detailed setup instructions
- **[User Guide](docs/user-guide.md)** - How to use Browser Agent
- **[Quick Start Examples](examples/)** - Ready-to-run examples

### 🔧 Development
- **[Contributing Guide](docs/CONTRIBUTING.md)** - How to contribute
- **[API Documentation](docs/api.md)** - API reference
- **[Plugin Development](docs/plugins.md)** - Creating custom plugins

### 🚀 Deployment
- **[Docker Guide](deployment/README.md)** - Container deployment
- **[Kubernetes Guide](deployment/kubernetes/)** - K8s deployment
- **[Cloud Deployment](docs/cloud-deployment.md)** - AWS, GCP, Azure

### 📋 Reference
- **[Configuration Reference](config/README.md)** - All configuration options
- **[Testing Guide](tests/README.md)** - Running and writing tests
- **[Troubleshooting](docs/troubleshooting.md)** - Common issues & solutions

## 🛠️ Development

### Prerequisites
- Python 3.8+ (3.11 recommended)
- Node.js 16+ (for web components)
- Docker (for containerized development)
- Git

### Development Workflow

```bash
# 1. Fork and clone the repository
git clone https://github.com/your-username/browser-agent.git
cd browser-agent

# 2. Set up development environment
make dev-install

# 3. Create feature branch
git checkout -b feature/your-feature-name

# 4. Make changes and test
make test
make lint

# 5. Submit pull request
git push origin feature/your-feature-name
```

### Available Make Commands

```bash
make install        # Install dependencies
make dev-install    # Install dev dependencies
make test          # Run test suite
make lint          # Run code linting
make format        # Format code
make docs          # Build documentation
make clean         # Clean build artifacts
make docker-build  # Build Docker image
make docker-run    # Run in Docker
```

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### Ways to Contribute
- 🐛 **Report bugs** - Use our [bug report template](.github/ISSUE_TEMPLATE/bug_report.yml)
- 💡 **Suggest features** - Use our [feature request template](.github/ISSUE_TEMPLATE/feature_request.yml)
- 📝 **Improve documentation** - Help make our docs better
- 🔧 **Submit code** - Fix bugs or implement features
- 🧪 **Write tests** - Improve test coverage
- 🎨 **Design improvements** - UI/UX enhancements

### Getting Started
1. Read our [Contributing Guide](docs/CONTRIBUTING.md)
2. Check out [good first issues](https://github.com/your-username/browser-agent/labels/good%20first%20issue)
3. Join our [community discussions](https://github.com/your-username/browser-agent/discussions)

## 📊 Project Status

![Build Status](https://github.com/your-username/browser-agent/workflows/CI/badge.svg)
![Test Coverage](https://codecov.io/gh/your-username/browser-agent/branch/main/graph/badge.svg)
![License](https://img.shields.io/github/license/your-username/browser-agent)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Docker Pulls](https://img.shields.io/docker/pulls/your-username/browser-agent)

## 🔒 Security

Security is a top priority. Please see our [Security Policy](docs/SECURITY.md) for:
- Reporting security vulnerabilities
- Security best practices
- Supported versions

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

### Getting Help
1. 📖 **Check the documentation** in [`docs/`](docs/)
2. 🔍 **Search existing issues** on GitHub
3. 💬 **Join discussions** in our community forum
4. 🐛 **Report bugs** using issue templates
5. 💡 **Request features** using our feature template

### Community
- **GitHub Discussions** - General questions and community chat
- **Issues** - Bug reports and feature requests
- **Pull Requests** - Code contributions
- **Wiki** - Community-maintained documentation

## 🙏 Acknowledgments

- **Contributors** - Thanks to all our amazing contributors!
- **Open Source Community** - Built on the shoulders of giants
- **Browser Vendors** - For providing excellent automation APIs
- **AI Community** - For advancing the field of intelligent automation



---

---

<div align="center">

**[📚 Documentation](docs/) • [🚀 Quick Start](#-quick-start) • [🤝 Contributing](docs/CONTRIBUTING.md) • [🐛 Issues](https://github.com/your-username/browser-agent/issues) • [💬 Discussions](https://github.com/your-username/browser-agent/discussions)**

*Built with ❤️ for the automation community*

</div>