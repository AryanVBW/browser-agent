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

## 🎯 Overview

Browser Agent is an AI-powered web automation tool that lets you control browsers using natural language. Simply tell the AI what you want to accomplish, and it will intelligently navigate websites, fill forms, extract data, and perform complex web tasks.

### Key Features
- **🧠 Multi-AI Support**: OpenAI GPT, Claude, and Gemini models
- **🌐 Multi-Browser**: Chrome, Firefox, Edge, Safari support
- **🎨 Modern GUI**: Intuitive interface with real-time feedback
- **🔌 MCP Integration**: Model Context Protocol support
- **🧩 Plugin System**: Extensible architecture
- **🐳 Docker Ready**: Container and cloud deployment

---

## 🖼️ Screenshots

![Chat Interface](assets/img/chat.png)
![Brain/LLM Configuration](assets/img/Brain:LLM.png)
![Task Log](assets/img/tasklog.png)
![Settings](assets/img/settings.png)

---

## 🚀 Quick Start

### Option 1: Local Installation

```bash
# Clone the repository
git clone https://github.com/AryanVBW/browser-agent.git
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

- **[Contributing Guide](docs/CONTRIBUTING.md)** - How to contribute
- **[Examples](examples/)** - Ready-to-run examples
- **[Configuration](config/README.md)** - Configuration options
- **[Testing](tests/README.md)** - Running tests
- **[Deployment](deployment/README.md)** - Docker & cloud deployment

## 🛠️ Development

**Prerequisites:** Python 3.8+, Docker, Git

```bash
# Setup
git clone https://github.com/AryanVBW/browser-agent.git
cd browser-agent
make dev-install

# Development
make test          # Run tests
make lint          # Code linting
make format        # Format code
make docker-build  # Build Docker image
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



---

<div align="center">

**[📚 Documentation](docs/) • [🚀 Quick Start](#-quick-start) • [🤝 Contributing](docs/CONTRIBUTING.md) • [🐛 Issues](https://github.com/AryanVBW/browser-agent/issues) • [💬 Discussions](https://github.com/AryanVBW/browser-agent/discussions)**

*Built with ❤️ for the automation community*

</div>