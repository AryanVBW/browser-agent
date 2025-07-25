# Tests

This directory contains all test files and testing configuration for Browser Agent.

## Contents

### Test Configuration
- **[pytest.ini](pytest.ini)** - Pytest configuration and settings
- **[tox.ini](tox.ini)** - Tox configuration for multi-environment testing

### Test Files
- **[test_auth_tokens.py](test_auth_tokens.py)** - Authentication token tests
- **[test_dependency_fix.py](test_dependency_fix.py)** - Dependency management tests
- **[test_enhanced_browser.py](test_enhanced_browser.py)** - Enhanced browser functionality tests
- **[test_enhanced_integration.py](test_enhanced_integration.py)** - Integration tests
- **[test_install.py](test_install.py)** - Installation and setup tests
- **[test_mcp_setup.py](test_mcp_setup.py)** - MCP (Model Context Protocol) setup tests
- **[test_unified_automation.py](test_unified_automation.py)** - Unified automation tests

## Test Structure

The test suite is organized into several categories:

```
tests/
├── unit/              # Unit tests (isolated component tests)
├── integration/       # Integration tests (component interaction)
├── e2e/              # End-to-end tests (full workflow)
├── fixtures/         # Test fixtures and data
├── conftest.py       # Pytest configuration and shared fixtures
└── utils/            # Test utilities and helpers
```

## Running Tests

### Quick Test Commands

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=brouser_agent --cov-report=html

# Run specific test file
pytest tests/test_auth_tokens.py

# Run specific test method
pytest tests/test_auth_tokens.py::TestAuthTokens::test_token_validation

# Run tests with specific markers
pytest -m "not slow"
pytest -m "integration"
```

### Using Tox (Multi-Environment Testing)

```bash
# Run tests across all environments
tox

# Run specific environment
tox -e py311
tox -e lint
tox -e coverage

# List available environments
tox -l
```

### Test Categories

#### Unit Tests
- Test individual functions and methods
- Fast execution
- No external dependencies
- Mock external services

#### Integration Tests
- Test component interactions
- May use real services (with caution)
- Slower than unit tests
- Test data flow between components

#### End-to-End Tests
- Test complete user workflows
- Use real browsers and services
- Slowest tests
- Most comprehensive coverage

## Writing Tests

### Test Guidelines

1. **Follow naming conventions**:
   - Test files: `test_*.py`
   - Test classes: `TestClassName`
   - Test methods: `test_method_name`

2. **Use descriptive names**:
   ```python
   def test_browser_launches_successfully_with_valid_config(self):
       """Test that browser launches when given valid configuration."""
   ```

3. **Structure tests with AAA pattern**:
   ```python
   def test_example(self):
       # Arrange
       config = {"browser": "chrome", "headless": True}
       
       # Act
       result = launch_browser(config)
       
       # Assert
       assert result.is_running
   ```

4. **Use fixtures for setup**:
   ```python
   @pytest.fixture
   def browser_config():
       return {"browser": "chrome", "headless": True}
   
   def test_with_fixture(browser_config):
       result = launch_browser(browser_config)
       assert result.is_running
   ```

### Test Markers

Use pytest markers to categorize tests:

```python
@pytest.mark.unit
def test_unit_function():
    pass

@pytest.mark.integration
def test_integration_workflow():
    pass

@pytest.mark.slow
def test_long_running_process():
    pass

@pytest.mark.browser
def test_browser_automation():
    pass
```

### Mocking External Dependencies

```python
from unittest.mock import Mock, patch

@patch('brouser_agent.core.Browser')
def test_with_mock_browser(mock_browser):
    mock_browser.return_value.is_running = True
    result = some_function_using_browser()
    assert result.success
```

## Test Configuration

### Pytest Configuration (pytest.ini)

Key settings:
- Test discovery patterns
- Markers definition
- Coverage settings
- Output formatting

### Tox Configuration (tox.ini)

Environments:
- **py38, py39, py310, py311** - Python version testing
- **lint** - Code quality checks
- **type** - Type checking with mypy
- **coverage** - Coverage reporting
- **docs** - Documentation building

## Continuous Integration

Tests run automatically on:
- Pull requests
- Pushes to main branch
- Scheduled runs (nightly)

See `.github/workflows/` for CI configuration.

## Test Data and Fixtures

### Creating Test Data

```python
# conftest.py
@pytest.fixture
def sample_webpage():
    return {
        "url": "https://example.com",
        "title": "Example Domain",
        "content": "<html>...</html>"
    }
```

### Using Temporary Files

```python
import tempfile
from pathlib import Path

def test_file_operations():
    with tempfile.TemporaryDirectory() as temp_dir:
        test_file = Path(temp_dir) / "test.txt"
        test_file.write_text("test content")
        # Test file operations
```

## Performance Testing

### Benchmarking

```python
import time

def test_performance():
    start_time = time.time()
    # Operation to test
    end_time = time.time()
    
    execution_time = end_time - start_time
    assert execution_time < 1.0  # Should complete within 1 second
```

### Memory Testing

```python
import psutil
import os

def test_memory_usage():
    process = psutil.Process(os.getpid())
    initial_memory = process.memory_info().rss
    
    # Operation that might use memory
    
    final_memory = process.memory_info().rss
    memory_increase = final_memory - initial_memory
    
    # Assert memory usage is reasonable
    assert memory_increase < 100 * 1024 * 1024  # Less than 100MB
```

## Debugging Tests

### Running Tests in Debug Mode

```bash
# Run with verbose output
pytest -v

# Run with print statements
pytest -s

# Run with debugger
pytest --pdb

# Run specific test with debugging
pytest tests/test_file.py::test_function -v -s --pdb
```

### Test Logging

```python
import logging

def test_with_logging(caplog):
    with caplog.at_level(logging.INFO):
        # Code that logs
        pass
    
    assert "Expected log message" in caplog.text
```

## Best Practices

1. **Keep tests independent** - Each test should be able to run in isolation
2. **Use meaningful assertions** - Assert specific conditions, not just "truthy" values
3. **Test edge cases** - Include boundary conditions and error cases
4. **Keep tests fast** - Unit tests should run in milliseconds
5. **Clean up resources** - Use fixtures and context managers for cleanup
6. **Document complex tests** - Add docstrings explaining test purpose
7. **Avoid test interdependencies** - Tests should not rely on execution order

## Troubleshooting

### Common Issues

1. **Import errors** - Check PYTHONPATH and package structure
2. **Fixture not found** - Ensure fixtures are in conftest.py or imported
3. **Tests hanging** - Check for infinite loops or blocking operations
4. **Flaky tests** - Add proper waits and retries for timing-sensitive tests

### Getting Help

- Check test output and error messages
- Review [pytest documentation](https://docs.pytest.org/)
- See [../docs/CONTRIBUTING.md](../docs/CONTRIBUTING.md) for development guidelines
- Ask in project discussions or open an issue

---

**Remember:** Good tests are the foundation of reliable software. Write tests that you and your team can trust.