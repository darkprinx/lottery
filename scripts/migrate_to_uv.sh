#!/usr/bin/env bash

# Migration Script from pip to UV
# This script helps developers migrate from the old pip-based setup to UV

set -e

echo "=========================================="
echo "Migration from pip to UV"
echo "=========================================="
echo ""

# Step 1: Check if old virtual environment exists
if [ -d "venv" ] || [ -d "env" ] || [ -d ".venv" ]; then
    echo "✓ Found existing virtual environment"
    echo ""
    echo "Note: UV will create a new virtual environment (.venv)"
    echo "Your old environment will remain untouched for now."
    echo ""
fi

# Step 2: Check current Python packages
if [ -d "venv" ]; then
    echo "Current packages in venv:"
    ./venv/bin/pip list 2>/dev/null || echo "Could not list packages"
    echo ""
fi

# Step 3: Install UV if not present
if ! command -v uv &> /dev/null; then
    echo "UV is not installed. Installing..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.cargo/bin:$PATH"
    echo "✓ UV installed"
    echo ""
else
    echo "✓ UV is already installed"
    echo ""
fi

# Step 4: Initialize UV project
echo "Initializing UV project..."
uv sync
echo "✓ Dependencies installed with UV"
echo ""

# Step 5: Compare package versions
echo "Package comparison:"
echo "===================="
echo ""
echo "Old requirements.txt packages:"
cat requirements.txt 2>/dev/null || echo "No requirements.txt found"
echo ""
echo "New UV installed packages:"
uv pip list
echo ""

# Step 6: Test the new setup
echo "Testing new setup..."
echo "===================="
echo ""

# Test Django
echo "Testing Django..."
if uv run python manage.py check; then
    echo "✓ Django checks passed"
else
    echo "✗ Django checks failed"
    exit 1
fi

# Test pytest
echo ""
echo "Testing pytest..."
if uv run pytest --collect-only &>/dev/null; then
    echo "✓ Pytest can discover tests"
else
    echo "⚠ Pytest had issues (not critical)"
fi

echo ""
echo "=========================================="
echo "Migration Complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Review the changes in pyproject.toml"
echo "2. Test your application: make run"
echo "3. Run tests: make test"
echo "4. If everything works, you can remove:"
echo "   - Old virtual environment (venv/env)"
echo "   - requirements.txt (kept as backup)"
echo ""
echo "To activate UV environment:"
echo "  source .venv/bin/activate"
echo ""
echo "Or use UV directly:"
echo "  uv run python manage.py <command>"
echo ""
