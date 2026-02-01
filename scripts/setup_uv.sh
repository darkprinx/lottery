#!/usr/bin/env bash

# UV Setup Script for Lottery Project
# This script helps set up the project with UV for the first time

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging functions
log_info() {
    echo -e "${BLUE}ℹ ${NC} $1"
}

log_success() {
    echo -e "${GREEN}✓${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

log_error() {
    echo -e "${RED}✗${NC} $1"
}

# Print banner
echo -e "${BLUE}"
cat << "EOF"
╔═══════════════════════════════════════╗
║   Lottery Project - UV Setup          ║
╚═══════════════════════════════════════╝
EOF
echo -e "${NC}"

# Check if UV is installed
log_info "Checking if UV is installed..."
if command -v uv &> /dev/null; then
    UV_VERSION=$(uv --version)
    log_success "UV is installed: $UV_VERSION"
else
    log_warning "UV is not installed"
    echo ""
    read -p "Do you want to install UV? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        log_info "Installing UV..."
        curl -LsSf https://astral.sh/uv/install.sh | sh

        # Add UV to PATH for current session
        export PATH="$HOME/.cargo/bin:$PATH"

        if command -v uv &> /dev/null; then
            log_success "UV installed successfully!"
        else
            log_error "UV installation failed. Please install manually from: https://github.com/astral-sh/uv"
            exit 1
        fi
    else
        log_error "UV is required. Please install it from: https://github.com/astral-sh/uv"
        exit 1
    fi
fi

# Check Python version
log_info "Checking Python version..."
REQUIRED_PYTHON="3.11"
if [ -f .python-version ]; then
    REQUIRED_PYTHON=$(cat .python-version)
fi
log_info "Required Python version: $REQUIRED_PYTHON"

# Backup old requirements.txt if it exists
if [ -f requirements.txt ]; then
    log_warning "Found old requirements.txt"
    if [ ! -f requirements.txt.backup ]; then
        log_info "Creating backup: requirements.txt.backup"
        cp requirements.txt requirements.txt.backup
        log_success "Backup created"
    fi
fi

# Backup old virtual environment
if [ -d venv ] || [ -d env ]; then
    log_warning "Found old virtual environment"
    read -p "Do you want to remove it? (UV will create a new one) (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        rm -rf venv env
        log_success "Old virtual environment removed"
    fi
fi

# Remove old lock files
log_info "Cleaning up old dependency management files..."
[ -f Pipfile.lock ] && rm Pipfile.lock && log_info "Removed Pipfile.lock"
[ -f poetry.lock ] && rm poetry.lock && log_info "Removed poetry.lock"

# Sync dependencies with UV
log_info "Installing dependencies with UV..."
if uv sync; then
    log_success "Dependencies installed successfully!"
else
    log_error "Failed to install dependencies"
    exit 1
fi

# Install pre-commit hooks
log_info "Installing pre-commit hooks..."
if uv run pre-commit install; then
    log_success "Pre-commit hooks installed!"
else
    log_warning "Failed to install pre-commit hooks (not critical)"
fi

# Run Django checks
log_info "Running Django system checks..."
if uv run python src/manage.py check; then
    log_success "Django checks passed!"
else
    log_warning "Django checks found some issues (check output above)"
fi

# Check if database needs migration
log_info "Checking database..."
if [ -f db.sqlite3 ]; then
    log_info "Database exists"
    read -p "Do you want to run migrations? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        uv run python src/manage.py migrate
        log_success "Migrations applied!"
    fi
else
    log_info "No database found. Running initial migrations..."
    if uv run python src/manage.py migrate; then
        log_success "Initial database created!"

        read -p "Do you want to create a superuser? (y/n) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            uv run python src/manage.py createsuperuser
        fi
    else
        log_warning "Failed to create database"
    fi
fi

# Print summary
echo ""
echo -e "${GREEN}"
cat << "EOF"
╔═══════════════════════════════════════╗
║   Setup Complete! 🎉                  ║
╚═══════════════════════════════════════╝
EOF
echo -e "${NC}"

echo ""
log_success "Your development environment is ready!"
echo ""
echo -e "${BLUE}Next steps:${NC}"
echo "  1. Run 'make help' to see all available commands"
echo "  2. Run 'make run' to start the development server"
echo "  3. Run 'make test' to run tests"
echo "  4. Read UV_SETUP.md for detailed documentation"
echo ""
echo -e "${BLUE}Quick commands:${NC}"
echo "  make run              # Start Django server"
echo "  make test             # Run tests"
echo "  make lint             # Check code quality"
echo "  make format           # Format code"
echo "  make shell            # Start Django shell"
echo ""
echo -e "${YELLOW}Note:${NC} Use 'uv run' prefix for any Python command"
echo "Example: uv run python manage.py <command>"
echo ""
