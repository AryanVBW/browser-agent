# Documentation

This directory contains all project documentation for Browser Agent.

## Contents

### Core Documentation
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Complete guide for contributors
- **[CHANGELOG.md](CHANGELOG.md)** - Version history and release notes

### Feature Documentation
- **[MCP_README.md](MCP_README.md)** - Model Context Protocol integration
- **[MCP_AUTH_FEATURE.md](MCP_AUTH_FEATURE.md)** - Authentication features
- **[MCP_CUSTOM_SETUP.md](MCP_CUSTOM_SETUP.md)** - Custom MCP server setup

### Technical Documentation
- **[DEPENDENCY_FIX.md](DEPENDENCY_FIX.md)** - Dependency management and fixes

## Documentation Structure

For a complete documentation experience, also see:

- **[../README.md](../README.md)** - Main project README
- **[../examples/](../examples/)** - Code examples and demos
- **API Documentation** - Generated from code docstrings

## Building Documentation

To build the full documentation:

```bash
# Install documentation dependencies
pip install -e ".[docs]"

# Build documentation (if using Sphinx)
cd docs/
make html

# Or serve locally
make serve
```

## Contributing to Documentation

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:

- Writing documentation
- Documentation style guide
- Building and testing docs
- Submitting documentation improvements

## Documentation Standards

- **Clear and concise** - Write for your target audience
- **Include examples** - Show, don't just tell
- **Keep updated** - Documentation should match current code
- **Test examples** - Ensure all code examples work
- **Use consistent formatting** - Follow established patterns

---

**Need help?** Check the [CONTRIBUTING.md](CONTRIBUTING.md) guide or open an issue.