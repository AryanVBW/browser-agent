# Configuration

This directory contains configuration files, environment templates, and settings for Browser Agent.

## Contents

### Environment Configuration
- **[.env.example](.env.example)** - Environment variables template
- **[.pre-commit-config.yaml](.pre-commit-config.yaml)** - Pre-commit hooks configuration

### Application Configuration
- **[mcp_servers.json](mcp_servers.json)** - MCP (Model Context Protocol) server configurations
- **[task_history.json](task_history.json)** - Task execution history and state

## Configuration Files

### Environment Variables (.env.example)

Template for environment-specific settings. Copy to `.env` and customize:

```bash
# Copy template to create your environment file
cp config/.env.example .env

# Edit with your specific values
vim .env
```

**Important:** Never commit `.env` files with actual secrets to version control.

### MCP Server Configuration (mcp_servers.json)

Defines MCP server endpoints and settings:

```json
{
  "servers": {
    "server_name": {
      "command": "python",
      "args": ["path/to/server.py"],
      "env": {
        "API_KEY": "${API_KEY}"
      }
    }
  }
}
```

### Pre-commit Configuration (.pre-commit-config.yaml)

Defines code quality checks that run before commits:

- Code formatting (Black, isort)
- Linting (flake8, pylint)
- Type checking (mypy)
- Security scanning (bandit)
- Documentation checks

### Task History (task_history.json)

Stores execution history and state for task management:

```json
{
  "tasks": [
    {
      "id": "task_123",
      "timestamp": "2024-01-01T12:00:00Z",
      "status": "completed",
      "result": {...}
    }
  ]
}
```

## Configuration Management

### Environment-Specific Settings

1. **Development** - Use `.env` for local development
2. **Testing** - Override with test-specific values
3. **Production** - Use environment variables or secure vaults

### Configuration Hierarchy

Settings are loaded in this order (later values override earlier ones):

1. Default values in code
2. Configuration files
3. Environment variables
4. Command-line arguments

### Security Best Practices

#### Environment Variables

```bash
# Good: Use environment variables for secrets
export API_KEY="your-secret-key"
export DATABASE_URL="postgresql://..."

# Bad: Don't hardcode secrets in config files
# api_key = "your-secret-key"  # Never do this!
```

#### File Permissions

```bash
# Restrict access to sensitive config files
chmod 600 .env
chmod 644 config/*.json
```

#### Git Configuration

```gitignore
# .gitignore - Never commit these files
.env
.env.local
.env.production
*.key
*.pem
secrets/
```

## Configuration Schema

### Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `BROWSER_TYPE` | Default browser type | `chrome` | No |
| `HEADLESS` | Run browser in headless mode | `false` | No |
| `LOG_LEVEL` | Logging level | `INFO` | No |
| `API_KEY` | API key for external services | - | Yes |
| `DATABASE_URL` | Database connection string | - | No |
| `REDIS_URL` | Redis connection string | - | No |
| `DEBUG` | Enable debug mode | `false` | No |

### MCP Server Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "servers": {
      "type": "object",
      "patternProperties": {
        "^[a-zA-Z0-9_-]+$": {
          "type": "object",
          "properties": {
            "command": {"type": "string"},
            "args": {
              "type": "array",
              "items": {"type": "string"}
            },
            "env": {
              "type": "object",
              "additionalProperties": {"type": "string"}
            },
            "timeout": {"type": "number"},
            "retry_count": {"type": "number"}
          },
          "required": ["command"]
        }
      }
    }
  }
}
```

## Configuration Examples

### Development Environment

```bash
# .env
BROWSER_TYPE=chrome
HEADLESS=false
LOG_LEVEL=DEBUG
DEBUG=true
API_KEY=dev-api-key
```

### Production Environment

```bash
# Environment variables (not in file)
export BROWSER_TYPE=chrome
export HEADLESS=true
export LOG_LEVEL=INFO
export DEBUG=false
export API_KEY="$(cat /secrets/api-key)"
export DATABASE_URL="$(cat /secrets/db-url)"
```

### Testing Environment

```bash
# .env.test
BROWSER_TYPE=chrome
HEADLESS=true
LOG_LEVEL=WARNING
DEBUG=false
API_KEY=test-api-key
DATABASE_URL=sqlite:///test.db
```

## Configuration Validation

### Environment Validation

```python
import os
from typing import Optional

class Config:
    def __init__(self):
        self.browser_type = os.getenv('BROWSER_TYPE', 'chrome')
        self.headless = os.getenv('HEADLESS', 'false').lower() == 'true'
        self.log_level = os.getenv('LOG_LEVEL', 'INFO')
        self.api_key = os.getenv('API_KEY')
        
        self.validate()
    
    def validate(self):
        if not self.api_key:
            raise ValueError("API_KEY environment variable is required")
        
        if self.browser_type not in ['chrome', 'firefox', 'safari']:
            raise ValueError(f"Invalid browser type: {self.browser_type}")
```

### JSON Schema Validation

```python
import json
import jsonschema

def validate_mcp_config(config_path: str):
    with open(config_path) as f:
        config = json.load(f)
    
    schema = {
        "type": "object",
        "properties": {
            "servers": {"type": "object"}
        },
        "required": ["servers"]
    }
    
    jsonschema.validate(config, schema)
```

## Configuration Loading

### Python Configuration Loader

```python
import os
import json
from pathlib import Path
from typing import Dict, Any

class ConfigLoader:
    def __init__(self, config_dir: str = "config"):
        self.config_dir = Path(config_dir)
    
    def load_env(self, env_file: str = ".env") -> Dict[str, str]:
        """Load environment variables from file."""
        env_path = self.config_dir / env_file
        env_vars = {}
        
        if env_path.exists():
            with open(env_path) as f:
                for line in f:
                    if '=' in line and not line.startswith('#'):
                        key, value = line.strip().split('=', 1)
                        env_vars[key] = value.strip('"\'')
        
        return env_vars
    
    def load_json(self, json_file: str) -> Dict[str, Any]:
        """Load JSON configuration file."""
        json_path = self.config_dir / json_file
        
        if json_path.exists():
            with open(json_path) as f:
                return json.load(f)
        
        return {}
    
    def load_all(self) -> Dict[str, Any]:
        """Load all configuration files."""
        return {
            'env': self.load_env(),
            'mcp_servers': self.load_json('mcp_servers.json'),
            'task_history': self.load_json('task_history.json')
        }
```

## Troubleshooting

### Common Issues

1. **Missing environment variables**
   ```bash
   # Check if variable is set
   echo $API_KEY
   
   # Set temporarily
   export API_KEY="your-key"
   ```

2. **Invalid JSON configuration**
   ```bash
   # Validate JSON syntax
   python -m json.tool config/mcp_servers.json
   ```

3. **Permission denied**
   ```bash
   # Fix file permissions
   chmod 644 config/*.json
   chmod 600 .env
   ```

4. **Configuration not found**
   ```bash
   # Check file exists
   ls -la config/
   
   # Create from template
   cp config/.env.example .env
   ```

### Debugging Configuration

```python
import os
import json

def debug_config():
    print("Environment Variables:")
    for key, value in os.environ.items():
        if key.startswith(('BROWSER_', 'API_', 'LOG_')):
            print(f"  {key}={value}")
    
    print("\nConfiguration Files:")
    config_files = ['mcp_servers.json', 'task_history.json']
    for file in config_files:
        try:
            with open(f"config/{file}") as f:
                config = json.load(f)
                print(f"  {file}: {len(config)} keys")
        except Exception as e:
            print(f"  {file}: Error - {e}")
```

## Best Practices

1. **Use environment variables for secrets** - Never commit sensitive data
2. **Provide example files** - Include `.env.example` with dummy values
3. **Validate configuration** - Check required values and formats
4. **Document all settings** - Explain purpose and valid values
5. **Use consistent naming** - Follow naming conventions (UPPER_CASE for env vars)
6. **Set appropriate defaults** - Provide sensible fallback values
7. **Separate environments** - Use different configs for dev/test/prod
8. **Version control templates** - Commit example files, not actual configs

## Getting Help

- Check configuration file syntax and format
- Review environment variable names and values
- See [../docs/CONTRIBUTING.md](../docs/CONTRIBUTING.md) for development setup
- Open an issue for configuration-related problems

---

**Security Note:** Always review configuration files before committing to ensure no secrets are included.