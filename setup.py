#!/usr/bin/env python3
"""
Professional setup configuration for Browser Agent

This setup.py provides backward compatibility while the main
packaging configuration is now in pyproject.toml
"""

import sys
from pathlib import Path
from setuptools import setup

# Ensure Python version compatibility
if sys.version_info < (3, 8):
    sys.exit("Browser Agent requires Python 3.8 or higher")

# Read version from package
try:
    sys.path.insert(0, str(Path(__file__).parent))
    from brouser_agent import __version__, __author__, __description__
except ImportError:
    __version__ = "1.0.0"
    __author__ = "Browser Agent Team"
    __description__ = "Professional AI-Powered Web Browser Automation Platform"

# Read long description
readme_file = Path(__file__).parent / "README.md"
if readme_file.exists():
    with open(readme_file, "r", encoding="utf-8") as f:
        long_description = f.read()
else:
    long_description = __description__

# Read requirements
requirements_file = Path(__file__).parent / "requirements.txt"
if requirements_file.exists():
    with open(requirements_file, "r", encoding="utf-8") as f:
        requirements = [
            line.strip() 
            for line in f 
            if line.strip() and not line.startswith("#")
        ]
else:
    requirements = []

# Development requirements
dev_requirements = [
    "pytest>=7.0.0",
    "pytest-cov>=4.0.0",
    "black>=22.0.0",
    "flake8>=5.0.0",
    "mypy>=1.0.0",
    "pre-commit>=2.20.0",
]

# Documentation requirements
docs_requirements = [
    "sphinx>=5.0.0",
    "sphinx-rtd-theme>=1.0.0",
    "myst-parser>=0.18.0",
]

# Test requirements
test_requirements = [
    "pytest>=7.0.0",
    "pytest-cov>=4.0.0",
    "pytest-mock>=3.8.0",
    "pytest-asyncio>=0.20.0",
]

setup(
    name="brouser-agent",
    version=__version__,
    author=__author__,
    author_email="support@browser-agent.com",
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/browser-agent",
    project_urls={
        "Documentation": "https://browser-agent.readthedocs.io",
        "Source": "https://github.com/yourusername/browser-agent",
        "Tracker": "https://github.com/yourusername/browser-agent/issues",
        "Changelog": "https://github.com/yourusername/browser-agent/blob/main/CHANGELOG.md",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet :: WWW/HTTP :: Browsers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Testing",
        "Topic :: System :: Systems Administration",
        "Environment :: Console",
        "Environment :: X11 Applications",
        "Environment :: Win32 (MS Windows)",
        "Environment :: MacOS X",
    ],
    keywords=[
        "browser", "automation", "ai", "selenium", "playwright", 
        "web-scraping", "testing", "gui", "openai", "claude", "gemini"
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": dev_requirements,
        "docs": docs_requirements,
        "test": test_requirements,
        "all": dev_requirements + docs_requirements + test_requirements,
    },
    entry_points={
        "console_scripts": [
            "brouser-agent=brouser_agent.cli_main:main",
        ],
        "gui_scripts": [
            "brouser-agent-gui=brouser_agent.gui_main:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    platforms=["any"],
)