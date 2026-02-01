#!/usr/bin/env bash

# Quick start script for Lottery project with UV
# This provides a fast way to get started

set -e

echo "=========================================="
echo "  Lottery Project - Quick Start with UV"
echo "=========================================="
echo ""

# Check if UV is installed
if ! command -v uv &> /dev/null; then
    echo "❌ UV is not installed"
    echo ""
    echo "Install UV first:"
    echo "  curl -LsSf https://astral.sh/uv/install.sh | sh"
    echo ""
    echo "Then run this script again."
    exit 1
fi

echo "✓ UV is installed"
echo ""

# Check if dependencies are already installed
if [ ! -d ".venv" ]; then
    echo "📦 Installing dependencies..."
    uv sync
    echo ""
fi

# Install pre-commit if not already done
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "⚠ Not a git repository. Skipping pre-commit setup."
else
    echo "🔧 Setting up pre-commit hooks..."
    uv run pre-commit install
    echo ""
fi

# Check if database exists
if [ ! -f "db.sqlite3" ]; then
    echo "🗄️  Creating database..."
    uv run python src/manage.py migrate
    echo ""
    echo "Would you like to create a superuser? (yes/no)"
    read -r response
    if [ "$response" = "yes" ]; then
        uv run python src/manage.py createsuperuser
    fi
else
    echo "✓ Database exists"
    echo ""
fi

echo ""
echo "=========================================="
echo "  Setup Complete! 🎉"
echo "=========================================="
echo ""
echo "Quick Commands:"
echo "  make run          - Start development server"
echo "  make test         - Run tests"
echo "  make lint         - Check code quality"
echo "  make help         - Show all commands"
echo ""
echo "Or use UV directly:"
echo "  uv run python manage.py runserver"
echo ""
echo "Ready to start? Run:"
echo "  make run"
echo ""
