# Scripts

This directory contains utility scripts, fixes, and automation tools for Browser Agent.

## Contents

### Setup and Installation Scripts
- **[init.py](init.py)** - Project initialization script
- **[run_gui.py](run_gui.py)** - GUI application launcher

### Platform-Specific Launchers
- **[start.sh](start.sh)** - Unix/Linux/macOS startup script
- **[start.bat](start.bat)** - Windows startup script

### Fix and Maintenance Scripts
- **[fix_dependency_detection.py](fix_dependency_detection.py)** - Dependency detection fixes
- **[fix_placeholder_error.py](fix_placeholder_error.py)** - Placeholder error resolution
- **[quick_fix.py](quick_fix.py)** - Quick fixes for common issues

### MCP Integration Scripts
- **[mcp_custom_server.py](mcp_custom_server.py)** - Custom MCP server implementation

## Usage

### Running the GUI
```bash
# From project root
python scripts/run_gui.py

# Or use platform-specific launchers
./scripts/start.sh      # Unix/Linux/macOS
scripts\start.bat       # Windows
```

### Running Fix Scripts
```bash
# Fix dependency detection issues
python scripts/fix_dependency_detection.py

# Fix placeholder errors
python scripts/fix_placeholder_error.py

# Apply quick fixes
python scripts/quick_fix.py
```

### MCP Server Setup
```bash
# Start custom MCP server
python scripts/mcp_custom_server.py
```

## Script Guidelines

### Adding New Scripts

1. **Place in appropriate category** (setup, fix, platform, etc.)
2. **Add proper documentation** with docstrings
3. **Include usage examples** in script header
4. **Update this README** with new script info
5. **Make executable** if needed (`chmod +x script.sh`)

### Script Standards

- **Clear naming** - Use descriptive names
- **Error handling** - Handle failures gracefully
- **Logging** - Use proper logging for debugging
- **Cross-platform** - Consider OS differences
- **Documentation** - Include usage and examples

### Example Script Template

```python
#!/usr/bin/env python3
"""
Script Name: example_script.py
Description: Brief description of what this script does
Usage: python scripts/example_script.py [options]
Author: Browser Agent Team
"""

import sys
import logging
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    """Main script function."""
    try:
        # Script logic here
        logger.info("Script completed successfully")
    except Exception as e:
        logger.error(f"Script failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

## Troubleshooting

### Common Issues

1. **Permission denied** - Make scripts executable:
   ```bash
   chmod +x scripts/script_name.sh
   ```

2. **Module not found** - Ensure project root is in Python path:
   ```python
   sys.path.insert(0, str(Path(__file__).parent.parent))
   ```

3. **Platform compatibility** - Use `os.name` or `platform.system()` for OS-specific code

### Getting Help

- Check script documentation with `python script.py --help`
- Review logs for error details
- See [../docs/CONTRIBUTING.md](../docs/CONTRIBUTING.md) for development guidelines
- Open an issue for persistent problems

---

**Note:** Always test scripts in a development environment before using in production.