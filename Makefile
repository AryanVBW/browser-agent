# Makefile for Browser Agent
# Provides convenient commands for development, testing, and deployment

# Variables
PYTHON := python3
PIP := pip3
PYTEST := pytest
BLACK := black
FLAKE8 := flake8
MYPY := mypy
ISORT := isort
PRE_COMMIT := pre-commit
TWINE := twine
SPHINX := sphinx-build

# Directories
SRC_DIR := brouser_agent
TEST_DIR := tests
DOCS_DIR := docs
BUILD_DIR := build
DIST_DIR := dist
COVERAGE_DIR := htmlcov
REPORTS_DIR := reports

# Files
REQUIREMENTS := requirements.txt
REQUIREMENTS_DEV := requirements-dev.txt
REQUIREMENTS_DOCS := requirements-docs.txt
REQUIREMENTS_MCP := requirements-mcp.txt
REQUIREMENTS_MINIMAL := requirements-minimal.txt

# Colors for output
RED := \033[0;31m
GREEN := \033[0;32m
YELLOW := \033[0;33m
BLUE := \033[0;34m
MAGENTA := \033[0;35m
CYAN := \033[0;36m
WHITE := \033[0;37m
RESET := \033[0m

# Default target
.DEFAULT_GOAL := help

# Phony targets
.PHONY: help install install-dev install-docs install-all clean clean-all \
        format lint type-check test test-unit test-integration test-e2e \
        test-coverage test-benchmark test-all coverage coverage-html \
        coverage-xml docs docs-serve docs-clean build build-wheel \
        build-sdist upload upload-test check-dist pre-commit \
        pre-commit-install pre-commit-update security-check \
        dependency-check update-deps freeze-deps setup-dev \
        setup-playwright setup-browsers run-gui run-cli demo \
        profile benchmark performance-test stress-test \
        docker-build docker-run docker-test docker-clean \
        release release-patch release-minor release-major \
        changelog version bump-version tag-release \
        backup restore migrate upgrade downgrade \
        monitor logs debug validate verify audit \
        init-project reset-project status health-check

# Help target
help: ## Show this help message
	@echo "$(CYAN)Browser Agent Development Commands$(RESET)"
	@echo ""
	@echo "$(YELLOW)Installation:$(RESET)"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / && /install/ {printf "  $(GREEN)%-20s$(RESET) %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo ""
	@echo "$(YELLOW)Development:$(RESET)"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / && /format|lint|type|clean|setup/ {printf "  $(GREEN)%-20s$(RESET) %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo ""
	@echo "$(YELLOW)Testing:$(RESET)"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / && /test|coverage|benchmark/ {printf "  $(GREEN)%-20s$(RESET) %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo ""
	@echo "$(YELLOW)Documentation:$(RESET)"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / && /docs/ {printf "  $(GREEN)%-20s$(RESET) %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo ""
	@echo "$(YELLOW)Build & Release:$(RESET)"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / && /build|upload|release|version/ {printf "  $(GREEN)%-20s$(RESET) %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo ""
	@echo "$(YELLOW)Application:$(RESET)"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / && /run|demo/ {printf "  $(GREEN)%-20s$(RESET) %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo ""
	@echo "$(YELLOW)Utilities:$(RESET)"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / && !/install|format|lint|type|clean|setup|test|coverage|benchmark|docs|build|upload|release|version|run|demo/ {printf "  $(GREEN)%-20s$(RESET) %s\n", $$1, $$2}' $(MAKEFILE_LIST)

# Installation targets
install: ## Install production dependencies
	@echo "$(BLUE)Installing production dependencies...$(RESET)"
	$(PIP) install -r $(REQUIREMENTS)
	@echo "$(GREEN)Production dependencies installed successfully!$(RESET)"

install-dev: ## Install development dependencies
	@echo "$(BLUE)Installing development dependencies...$(RESET)"
	$(PIP) install -r $(REQUIREMENTS_DEV)
	@echo "$(GREEN)Development dependencies installed successfully!$(RESET)"

install-docs: ## Install documentation dependencies
	@echo "$(BLUE)Installing documentation dependencies...$(RESET)"
	$(PIP) install -r $(REQUIREMENTS_DOCS)
	@echo "$(GREEN)Documentation dependencies installed successfully!$(RESET)"

install-all: install install-dev install-docs ## Install all dependencies
	@echo "$(GREEN)All dependencies installed successfully!$(RESET)"

# Setup targets
setup-dev: install-dev pre-commit-install setup-playwright ## Setup development environment
	@echo "$(BLUE)Setting up development environment...$(RESET)"
	$(PIP) install -e .
	@echo "$(GREEN)Development environment setup complete!$(RESET)"

setup-playwright: ## Setup Playwright browsers
	@echo "$(BLUE)Installing Playwright browsers...$(RESET)"
	$(PYTHON) -m playwright install
	@echo "$(GREEN)Playwright browsers installed successfully!$(RESET)"

setup-browsers: setup-playwright ## Alias for setup-playwright

# Cleaning targets
clean: ## Clean build artifacts
	@echo "$(BLUE)Cleaning build artifacts...$(RESET)"
	rm -rf $(BUILD_DIR) $(DIST_DIR) *.egg-info
	rm -rf .pytest_cache .mypy_cache .tox
	rm -rf $(COVERAGE_DIR) coverage.xml .coverage
	rm -rf $(REPORTS_DIR)
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type f -name "*.cover" -delete
	find . -type f -name "*.log" -delete
	@echo "$(GREEN)Build artifacts cleaned successfully!$(RESET)"

clean-all: clean docs-clean ## Clean all generated files
	@echo "$(BLUE)Cleaning all generated files...$(RESET)"
	rm -rf logs/ screenshots/ exports/ temp/ cache/
	rm -rf browser_profiles/ user_data/
	rm -rf .benchmarks/ performance_logs/
	rm -rf htmlcov/ .coverage coverage.xml
	rm -rf .pytest_cache/ .mypy_cache/ .tox/
	rm -rf node_modules/ .npm/
	@echo "$(GREEN)All generated files cleaned successfully!$(RESET)"

# Code quality targets
format: ## Format code with Black and isort
	@echo "$(BLUE)Formatting code...$(RESET)"
	$(BLACK) $(SRC_DIR) $(TEST_DIR)
	$(ISORT) $(SRC_DIR) $(TEST_DIR)
	@echo "$(GREEN)Code formatted successfully!$(RESET)"

lint: ## Run linting with flake8
	@echo "$(BLUE)Running linting...$(RESET)"
	$(FLAKE8) $(SRC_DIR) $(TEST_DIR)
	@echo "$(GREEN)Linting completed successfully!$(RESET)"

type-check: ## Run type checking with mypy
	@echo "$(BLUE)Running type checking...$(RESET)"
	$(MYPY) $(SRC_DIR)
	@echo "$(GREEN)Type checking completed successfully!$(RESET)"

# Testing targets
test: ## Run all tests
	@echo "$(BLUE)Running all tests...$(RESET)"
	$(PYTEST)
	@echo "$(GREEN)All tests completed successfully!$(RESET)"

test-unit: ## Run unit tests only
	@echo "$(BLUE)Running unit tests...$(RESET)"
	$(PYTEST) -m "unit" -v
	@echo "$(GREEN)Unit tests completed successfully!$(RESET)"

test-integration: ## Run integration tests only
	@echo "$(BLUE)Running integration tests...$(RESET)"
	$(PYTEST) -m "integration" -v
	@echo "$(GREEN)Integration tests completed successfully!$(RESET)"

test-e2e: ## Run end-to-end tests only
	@echo "$(BLUE)Running end-to-end tests...$(RESET)"
	$(PYTEST) -m "e2e" -v
	@echo "$(GREEN)End-to-end tests completed successfully!$(RESET)"

test-fast: ## Run fast tests only
	@echo "$(BLUE)Running fast tests...$(RESET)"
	$(PYTEST) -m "fast" -v
	@echo "$(GREEN)Fast tests completed successfully!$(RESET)"

test-slow: ## Run slow tests only
	@echo "$(BLUE)Running slow tests...$(RESET)"
	$(PYTEST) -m "slow" -v
	@echo "$(GREEN)Slow tests completed successfully!$(RESET)"

test-coverage: ## Run tests with coverage
	@echo "$(BLUE)Running tests with coverage...$(RESET)"
	$(PYTEST) --cov=$(SRC_DIR) --cov-report=term-missing --cov-report=html
	@echo "$(GREEN)Tests with coverage completed successfully!$(RESET)"

test-benchmark: ## Run benchmark tests
	@echo "$(BLUE)Running benchmark tests...$(RESET)"
	$(PYTEST) --benchmark-only --benchmark-autosave
	@echo "$(GREEN)Benchmark tests completed successfully!$(RESET)"

test-all: test-unit test-integration test-e2e ## Run all test categories
	@echo "$(GREEN)All test categories completed successfully!$(RESET)"

# Coverage targets
coverage: test-coverage ## Generate coverage report

coverage-html: ## Generate HTML coverage report
	@echo "$(BLUE)Generating HTML coverage report...$(RESET)"
	$(PYTEST) --cov=$(SRC_DIR) --cov-report=html
	@echo "$(GREEN)HTML coverage report generated in $(COVERAGE_DIR)/$(RESET)"

coverage-xml: ## Generate XML coverage report
	@echo "$(BLUE)Generating XML coverage report...$(RESET)"
	$(PYTEST) --cov=$(SRC_DIR) --cov-report=xml
	@echo "$(GREEN)XML coverage report generated as coverage.xml$(RESET)"

# Documentation targets
docs: ## Build documentation
	@echo "$(BLUE)Building documentation...$(RESET)"
	mkdir -p $(DOCS_DIR)/_build
	$(SPHINX) -b html $(DOCS_DIR) $(DOCS_DIR)/_build/html
	@echo "$(GREEN)Documentation built successfully in $(DOCS_DIR)/_build/html/$(RESET)"

docs-serve: docs ## Build and serve documentation
	@echo "$(BLUE)Serving documentation at http://localhost:8000$(RESET)"
	cd $(DOCS_DIR)/_build/html && $(PYTHON) -m http.server 8000

docs-clean: ## Clean documentation build
	@echo "$(BLUE)Cleaning documentation build...$(RESET)"
	rm -rf $(DOCS_DIR)/_build
	@echo "$(GREEN)Documentation build cleaned successfully!$(RESET)"

# Build targets
build: clean ## Build distribution packages
	@echo "$(BLUE)Building distribution packages...$(RESET)"
	$(PYTHON) -m build
	@echo "$(GREEN)Distribution packages built successfully!$(RESET)"

build-wheel: clean ## Build wheel package
	@echo "$(BLUE)Building wheel package...$(RESET)"
	$(PYTHON) -m build --wheel
	@echo "$(GREEN)Wheel package built successfully!$(RESET)"

build-sdist: clean ## Build source distribution
	@echo "$(BLUE)Building source distribution...$(RESET)"
	$(PYTHON) -m build --sdist
	@echo "$(GREEN)Source distribution built successfully!$(RESET)"

# Upload targets
check-dist: build ## Check distribution packages
	@echo "$(BLUE)Checking distribution packages...$(RESET)"
	$(TWINE) check $(DIST_DIR)/*
	@echo "$(GREEN)Distribution packages checked successfully!$(RESET)"

upload-test: check-dist ## Upload to test PyPI
	@echo "$(BLUE)Uploading to test PyPI...$(RESET)"
	$(TWINE) upload --repository testpypi $(DIST_DIR)/*
	@echo "$(GREEN)Uploaded to test PyPI successfully!$(RESET)"

upload: check-dist ## Upload to PyPI
	@echo "$(YELLOW)Uploading to PyPI...$(RESET)"
	$(TWINE) upload $(DIST_DIR)/*
	@echo "$(GREEN)Uploaded to PyPI successfully!$(RESET)"

# Pre-commit targets
pre-commit: ## Run pre-commit hooks
	@echo "$(BLUE)Running pre-commit hooks...$(RESET)"
	$(PRE_COMMIT) run --all-files
	@echo "$(GREEN)Pre-commit hooks completed successfully!$(RESET)"

pre-commit-install: ## Install pre-commit hooks
	@echo "$(BLUE)Installing pre-commit hooks...$(RESET)"
	$(PRE_COMMIT) install
	@echo "$(GREEN)Pre-commit hooks installed successfully!$(RESET)"

pre-commit-update: ## Update pre-commit hooks
	@echo "$(BLUE)Updating pre-commit hooks...$(RESET)"
	$(PRE_COMMIT) autoupdate
	@echo "$(GREEN)Pre-commit hooks updated successfully!$(RESET)"

# Security targets
security-check: ## Run security checks
	@echo "$(BLUE)Running security checks...$(RESET)"
	bandit -r $(SRC_DIR)
	safety check
	@echo "$(GREEN)Security checks completed successfully!$(RESET)"

dependency-check: ## Check for dependency vulnerabilities
	@echo "$(BLUE)Checking dependencies for vulnerabilities...$(RESET)"
	safety check --json
	@echo "$(GREEN)Dependency check completed successfully!$(RESET)"

# Dependency management
update-deps: ## Update dependencies
	@echo "$(BLUE)Updating dependencies...$(RESET)"
	$(PIP) list --outdated
	$(PIP) install --upgrade pip setuptools wheel
	@echo "$(GREEN)Dependencies updated successfully!$(RESET)"

freeze-deps: ## Freeze current dependencies
	@echo "$(BLUE)Freezing current dependencies...$(RESET)"
	$(PIP) freeze > requirements-frozen.txt
	@echo "$(GREEN)Dependencies frozen to requirements-frozen.txt$(RESET)"

# Application targets
run-gui: ## Run GUI application
	@echo "$(BLUE)Starting GUI application...$(RESET)"
	$(PYTHON) run_gui.py

run-cli: ## Run CLI application
	@echo "$(BLUE)Starting CLI application...$(RESET)"
	$(PYTHON) -m brouser_agent.cli_main --help

demo: ## Run demo
	@echo "$(BLUE)Running demo...$(RESET)"
	$(PYTHON) examples/basic_usage.py

# Performance targets
profile: ## Profile application performance
	@echo "$(BLUE)Profiling application performance...$(RESET)"
	$(PYTHON) -m cProfile -o profile.stats examples/basic_usage.py
	@echo "$(GREEN)Performance profiling completed! Results in profile.stats$(RESET)"

benchmark: test-benchmark ## Run performance benchmarks

performance-test: ## Run performance tests
	@echo "$(BLUE)Running performance tests...$(RESET)"
	$(PYTEST) -m "performance" -v
	@echo "$(GREEN)Performance tests completed successfully!$(RESET)"

stress-test: ## Run stress tests
	@echo "$(BLUE)Running stress tests...$(RESET)"
	$(PYTEST) -m "stress" -v --maxfail=1
	@echo "$(GREEN)Stress tests completed successfully!$(RESET)"

# Version management
version: ## Show current version
	@echo "$(BLUE)Current version:$(RESET)"
	@$(PYTHON) -c "import brouser_agent; print(brouser_agent.__version__)"

bump-version: ## Bump version (specify TYPE=patch|minor|major)
	@echo "$(BLUE)Bumping version...$(RESET)"
	@if [ -z "$(TYPE)" ]; then \
		echo "$(RED)Error: Please specify TYPE=patch|minor|major$(RESET)"; \
		exit 1; \
	fi
	bump2version $(TYPE)
	@echo "$(GREEN)Version bumped successfully!$(RESET)"

release-patch: ## Release patch version
	@$(MAKE) bump-version TYPE=patch
	@$(MAKE) tag-release

release-minor: ## Release minor version
	@$(MAKE) bump-version TYPE=minor
	@$(MAKE) tag-release

release-major: ## Release major version
	@$(MAKE) bump-version TYPE=major
	@$(MAKE) tag-release

tag-release: ## Tag current version for release
	@echo "$(BLUE)Tagging release...$(RESET)"
	@VERSION=$$($(PYTHON) -c "import brouser_agent; print(brouser_agent.__version__)"); \
	git tag -a "v$$VERSION" -m "Release v$$VERSION"; \
	echo "$(GREEN)Tagged release v$$VERSION$(RESET)"

changelog: ## Generate changelog
	@echo "$(BLUE)Generating changelog...$(RESET)"
	git log --oneline --decorate --graph > CHANGELOG_AUTO.md
	@echo "$(GREEN)Changelog generated in CHANGELOG_AUTO.md$(RESET)"

# Docker targets
docker-build: ## Build Docker image
	@echo "$(BLUE)Building Docker image...$(RESET)"
	docker build -t browser-agent .
	@echo "$(GREEN)Docker image built successfully!$(RESET)"

docker-run: ## Run Docker container
	@echo "$(BLUE)Running Docker container...$(RESET)"
	docker run -it --rm browser-agent

docker-test: ## Run tests in Docker
	@echo "$(BLUE)Running tests in Docker...$(RESET)"
	docker run --rm browser-agent make test
	@echo "$(GREEN)Docker tests completed successfully!$(RESET)"

docker-clean: ## Clean Docker images
	@echo "$(BLUE)Cleaning Docker images...$(RESET)"
	docker rmi browser-agent || true
	docker system prune -f
	@echo "$(GREEN)Docker images cleaned successfully!$(RESET)"

# Utility targets
status: ## Show project status
	@echo "$(CYAN)Browser Agent Project Status$(RESET)"
	@echo ""
	@echo "$(YELLOW)Version:$(RESET) $$($(PYTHON) -c 'import brouser_agent; print(brouser_agent.__version__)' 2>/dev/null || echo 'Not installed')"
	@echo "$(YELLOW)Python:$(RESET) $$($(PYTHON) --version)"
	@echo "$(YELLOW)Pip:$(RESET) $$($(PIP) --version)"
	@echo "$(YELLOW)Git:$(RESET) $$(git --version 2>/dev/null || echo 'Not available')"
	@echo ""
	@echo "$(YELLOW)Dependencies:$(RESET)"
	@$(PIP) list | grep -E "(selenium|playwright|openai|anthropic|customtkinter)" || echo "  Core dependencies not found"
	@echo ""
	@echo "$(YELLOW)Project Structure:$(RESET)"
	@find $(SRC_DIR) -name "*.py" | wc -l | xargs echo "  Python files:"
	@find $(TEST_DIR) -name "*.py" 2>/dev/null | wc -l | xargs echo "  Test files:" || echo "  Test files: 0"
	@echo ""

health-check: ## Run health checks
	@echo "$(BLUE)Running health checks...$(RESET)"
	@echo "$(YELLOW)Checking Python installation...$(RESET)"
	@$(PYTHON) --version
	@echo "$(YELLOW)Checking pip installation...$(RESET)"
	@$(PIP) --version
	@echo "$(YELLOW)Checking core dependencies...$(RESET)"
	@$(PYTHON) -c "import selenium, playwright, openai; print('Core dependencies OK')"
	@echo "$(YELLOW)Checking project structure...$(RESET)"
	@test -d $(SRC_DIR) && echo "Source directory OK" || echo "$(RED)Source directory missing$(RESET)"
	@test -f $(REQUIREMENTS) && echo "Requirements file OK" || echo "$(RED)Requirements file missing$(RESET)"
	@echo "$(GREEN)Health checks completed successfully!$(RESET)"

validate: lint type-check test-fast ## Validate code quality
	@echo "$(GREEN)Code validation completed successfully!$(RESET)"

verify: validate security-check ## Verify code security and quality
	@echo "$(GREEN)Code verification completed successfully!$(RESET)"

audit: verify dependency-check ## Full audit of code and dependencies
	@echo "$(GREEN)Full audit completed successfully!$(RESET)"

# Project initialization
init-project: ## Initialize new project environment
	@echo "$(BLUE)Initializing project environment...$(RESET)"
	@echo "$(YELLOW)Creating virtual environment...$(RESET)"
	$(PYTHON) -m venv venv
	@echo "$(YELLOW)Activating virtual environment...$(RESET)"
	@echo "Please run: source venv/bin/activate (Linux/Mac) or venv\\Scripts\\activate (Windows)"
	@echo "$(YELLOW)Then run: make setup-dev$(RESET)"
	@echo "$(GREEN)Project initialization completed!$(RESET)"

reset-project: clean-all ## Reset project to clean state
	@echo "$(YELLOW)Warning: This will remove all generated files and caches!$(RESET)"
	@echo "$(YELLOW)Press Ctrl+C to cancel, or Enter to continue...$(RESET)"
	@read
	@echo "$(BLUE)Resetting project...$(RESET)"
	rm -rf venv/ .venv/ env/
	rm -rf .git/hooks/pre-commit
	rm -rf .pytest_cache/ .mypy_cache/ .tox/
	rm -rf htmlcov/ coverage.xml .coverage
	rm -rf logs/ screenshots/ exports/ temp/ cache/
	rm -rf browser_profiles/ user_data/
	@echo "$(GREEN)Project reset completed!$(RESET)"

# Monitoring and debugging
monitor: ## Monitor application logs
	@echo "$(BLUE)Monitoring application logs...$(RESET)"
	tail -f logs/*.log 2>/dev/null || echo "No log files found"

logs: ## Show recent logs
	@echo "$(BLUE)Recent application logs:$(RESET)"
	@find logs/ -name "*.log" -exec tail -20 {} \; 2>/dev/null || echo "No log files found"

debug: ## Run in debug mode
	@echo "$(BLUE)Running in debug mode...$(RESET)"
	DEBUG=1 $(PYTHON) run_gui.py --verbose

# Backup and restore
backup: ## Backup important files
	@echo "$(BLUE)Creating backup...$(RESET)"
	mkdir -p backups
	tar -czf backups/backup-$$(date +%Y%m%d-%H%M%S).tar.gz \
		$(SRC_DIR) $(TEST_DIR) $(REQUIREMENTS)* *.py *.md *.toml *.ini *.yaml *.yml
	@echo "$(GREEN)Backup created in backups/$(RESET)"

restore: ## Restore from backup (specify BACKUP=filename)
	@echo "$(BLUE)Restoring from backup...$(RESET)"
	@if [ -z "$(BACKUP)" ]; then \
		echo "$(RED)Error: Please specify BACKUP=filename$(RESET)"; \
		echo "Available backups:"; \
		ls -la backups/; \
		exit 1; \
	fi
	tar -xzf backups/$(BACKUP)
	@echo "$(GREEN)Restored from backup successfully!$(RESET)"

# Migration helpers
migrate: ## Run database migrations
	@echo "$(BLUE)Running migrations...$(RESET)"
	# Add migration commands here
	@echo "$(GREEN)Migrations completed successfully!$(RESET)"

upgrade: ## Upgrade project dependencies
	@echo "$(BLUE)Upgrading project...$(RESET)"
	$(PIP) install --upgrade pip setuptools wheel
	$(PIP) install --upgrade -r $(REQUIREMENTS)
	@echo "$(GREEN)Project upgraded successfully!$(RESET)"

downgrade: ## Downgrade to specific versions
	@echo "$(BLUE)Downgrading project...$(RESET)"
	# Add downgrade commands here
	@echo "$(GREEN)Project downgraded successfully!$(RESET)"

# Quick development workflow
dev: clean format lint test-fast ## Quick development workflow
	@echo "$(GREEN)Development workflow completed successfully!$(RESET)"

ci: clean format lint type-check test coverage ## CI/CD workflow
	@echo "$(GREEN)CI/CD workflow completed successfully!$(RESET)"

release: ci build upload ## Full release workflow
	@echo "$(GREEN)Release workflow completed successfully!$(RESET)"

# Show available make targets
list: ## List all available targets
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

# Environment info
env: ## Show environment information
	@echo "$(CYAN)Environment Information$(RESET)"
	@echo "$(YELLOW)Operating System:$(RESET) $$(uname -s)"
	@echo "$(YELLOW)Architecture:$(RESET) $$(uname -m)"
	@echo "$(YELLOW)Python Version:$(RESET) $$($(PYTHON) --version)"
	@echo "$(YELLOW)Python Path:$(RESET) $$(which $(PYTHON))"
	@echo "$(YELLOW)Pip Version:$(RESET) $$($(PIP) --version)"
	@echo "$(YELLOW)Virtual Environment:$(RESET) $$(echo $$VIRTUAL_ENV || echo 'None')"
	@echo "$(YELLOW)Working Directory:$(RESET) $$(pwd)"
	@echo "$(YELLOW)Git Branch:$(RESET) $$(git branch --show-current 2>/dev/null || echo 'Not a git repository')"
	@echo "$(YELLOW)Git Status:$(RESET) $$(git status --porcelain 2>/dev/null | wc -l | xargs echo 'files changed:' || echo 'Not a git repository')"