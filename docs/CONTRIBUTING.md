 # Contributing to Browser Agent

Thank you for your interest in contributing to Browser Agent! We welcome contributions from everyone, whether you're fixing a bug, adding a feature, improving documentation, or helping with community support.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Contributing Guidelines](#contributing-guidelines)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Documentation](#documentation)
- [Community](#community)
- [Recognition](#recognition)

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to [conduct@browser-agent.org](mailto:conduct@browser-agent.org).

## Getting Started

### Ways to Contribute

There are many ways to contribute to Browser Agent:

- **🐛 Report bugs** - Help us identify and fix issues
- **✨ Suggest features** - Propose new functionality
- **💻 Write code** - Implement features, fix bugs, improve performance
- **📚 Improve documentation** - Help others understand and use the project
- **🧪 Write tests** - Improve test coverage and quality
- **🎨 Design** - Improve UI/UX, create graphics, design workflows
- **🌐 Translate** - Help make the project accessible in more languages
- **💬 Community support** - Help other users in discussions and issues
- **📢 Spread the word** - Blog, tweet, or speak about the project

### First-Time Contributors

New to open source? Here are some good first issues:

- Look for issues labeled [`good first issue`](https://github.com/browser-agent/browser-agent/labels/good%20first%20issue)
- Check out [`help wanted`](https://github.com/browser-agent/browser-agent/labels/help%20wanted) issues
- Browse [`documentation`](https://github.com/browser-agent/browser-agent/labels/documentation) issues

### Before You Start

1. **Check existing issues** - Someone might already be working on it
2. **Read the documentation** - Understand how the project works
3. **Join our community** - Get help and discuss your ideas
4. **Start small** - Begin with small contributions to get familiar with the process

### Prerequisites

- **Python 3.8+** (3.11+ recommended)
- **Git**
- **Node.js 16+** (for web interface development)
- **Docker** (optional, for containerized development)

### Quick Setup

1. **Fork and clone the repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/browser-agent.git
   cd browser-agent
   ```

2. **Set up development environment**:
   ```bash
   make dev-setup
   ```

3. **Activate virtual environment**:
   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install in development mode**:
   ```bash
   make install-dev
   ```

5. **Run tests to verify setup**:
   ```bash
   make test
   ```

### Manual Setup

If you prefer manual setup:

1. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -e ".[dev,test,docs]"
   ```

3. **Install pre-commit hooks**:
   ```bash
   pre-commit install
   ```

4. **Install Playwright browsers**:
   ```bash
   playwright install
   ```

### Docker Development

For containerized development:

```bash
# Build development image
make docker-build-dev

# Run development container
make docker-dev

# Run tests in container
make docker-test
```

## Contributing Guidelines

### Issue Guidelines

#### Reporting Bugs

1. **Use the bug report template**
2. **Search existing issues** first
3. **Provide minimal reproduction** steps
4. **Include environment details**
5. **Add relevant labels**

#### Suggesting Features

1. **Use the feature request template**
2. **Explain the problem** you're trying to solve
3. **Describe your proposed solution**
4. **Consider alternatives**
5. **Think about implementation** complexity

#### Asking Questions

1. **Use the question template**
2. **Check documentation** first
3. **Search existing discussions**
4. **Provide context** about your use case
5. **Be specific** about what you need help with

### Code Contribution Workflow

1. **Create an issue** (if one doesn't exist)
2. **Fork the repository**
3. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Make your changes**
5. **Write/update tests**
6. **Update documentation**
7. **Run the test suite**:
   ```bash
   make test-all
   ```
8. **Commit your changes**:
   ```bash
   git commit -m "feat: add your feature description"
   ```
9. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```
10. **Create a pull request**

### Branch Naming

Use descriptive branch names:

- `feature/add-chrome-extension-support`
- `fix/memory-leak-in-browser-pool`
- `docs/update-installation-guide`
- `test/add-integration-tests`
- `refactor/simplify-config-system`

### Commit Messages

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```
type(scope): description

[optional body]

[optional footer]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks
- `perf`: Performance improvements
- `ci`: CI/CD changes
- `build`: Build system changes

**Examples:**
```
feat(browser): add support for Firefox profiles

fix(ai): resolve memory leak in OpenAI integration

docs(readme): update installation instructions

test(core): add unit tests for browser pool
```

## Pull Request Process

### Before Submitting

1. **Ensure all tests pass**:
   ```bash
   make test-all
   ```

2. **Run code quality checks**:
   ```bash
   make lint
   make type-check
   ```

3. **Update documentation** if needed

4. **Add/update tests** for your changes

5. **Rebase on latest main**:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

### PR Requirements

- [ ] **Clear description** of changes
- [ ] **Link to related issue(s)**
- [ ] **Tests added/updated**
- [ ] **Documentation updated**
- [ ] **All CI checks pass**
- [ ] **Code review completed**
- [ ] **Maintainer approval**

### Review Process

1. **Automated checks** run first
2. **Community review** (optional but encouraged)
3. **Maintainer review** (required)
4. **Address feedback** if needed
5. **Final approval** and merge

### After Your PR is Merged

1. **Delete your feature branch**
2. **Update your fork**:
   ```bash
   git checkout main
   git pull upstream main
   git push origin main
   ```
3. **Celebrate!** 🎉

## Development Setup

### Prerequisites

- **Python 3.8+** (3.11+ recommended)
- **Git**
- **Node.js 16+** (for web interface development)
- **Docker** (optional, for containerized development)

### Quick Setup

1. **Fork and clone the repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/browser-agent.git
   cd browser-agent
   ```

2. **Set up development environment**:
   ```bash
   make dev-setup
   ```

3. **Activate virtual environment**:
   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install in development mode**:
   ```bash
   make install-dev
   ```

5. **Run tests to verify setup**:
   ```bash
   make test
   ```

### Manual Setup

If you prefer manual setup:

1. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -e ".[dev,test,docs]"
   ```

3. **Install pre-commit hooks**:
   ```bash
   pre-commit install
   ```

4. **Install Playwright browsers**:
   ```bash
   playwright install
   ```

### Docker Development

For containerized development:

```bash
# Build development image
make docker-build-dev

# Run development container
make docker-dev

# Run tests in container
make docker-test
```

### Running Tests

```bash
# Run all tests
make test

# Run with coverage
make test-coverage

# Run specific test file
pytest tests/test_config/test_settings.py

# Run with verbose output
pytest -v

# Run integration tests
make test-integration

# Run performance tests
make test-performance
```

### Code Quality

We use several tools to maintain code quality:

#### Code Formatting
```bash
# Format code with Black
make format

# Check formatting
make format-check
```

#### Linting
```bash
# Run all linting
make lint

# Run specific linters
make lint-flake8
make lint-mypy
make lint-bandit
```

#### Pre-commit Hooks
Pre-commit hooks will automatically run when you commit:
```bash
# Run manually
pre-commit run --all-files

# Update hooks
pre-commit autoupdate
```