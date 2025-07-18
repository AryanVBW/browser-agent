#!/bin/bash

# Browser Agent Quick Start Script
# This script provides one-command initialization and launch

echo "🤖 Browser Agent - Quick Start"
echo "=============================="

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed"
    echo "   Please install Python 3.8+ and try again"
    exit 1
fi

echo "✅ Python found: $(python3 --version)"

# Check if we're in the right directory
if [ ! -f "requirements.txt" ]; then
    echo "❌ requirements.txt not found"
    echo "   Please run this script from the brouser-agent directory"
    exit 1
fi

echo "✅ In correct directory"

# Run initialization
echo ""
echo "🚀 Running initialization..."
python3 init.py

echo ""
echo "🎉 Browser Agent setup complete!"
echo ""
echo "Quick commands:"
echo "  python3 run_gui.py        # Launch GUI"
echo "  python3 init.py           # Re-run setup"
echo "  ./start.sh                # This script"