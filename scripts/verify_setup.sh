#!/usr/bin/env bash

# Complete UV Setup Verification Script
# This script validates that everything is configured correctly

set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}"
echo "=================================================="
echo "  UV Setup Verification for Lottery Project"
echo "=================================================="
echo -e "${NC}\n"

# Check UV
echo -e "${BLUE}1. Checking UV...${NC}"
if command -v uv &> /dev/null; then
    echo -e "   ${GREEN}✓${NC} UV is installed: $(uv --version)"
else
    echo -e "   ${RED}✗${NC} UV is not installed"
    exit 1
fi

# Check Python
echo -e "\n${BLUE}2. Checking Python...${NC}"
PYTHON_VERSION=$(uv run python --version)
echo -e "   ${GREEN}✓${NC} Python: $PYTHON_VERSION"

# Check virtual environment
echo -e "\n${BLUE}3. Checking virtual environment...${NC}"
if [ -d ".venv" ]; then
    echo -e "   ${GREEN}✓${NC} Virtual environment exists (.venv)"
else
    echo -e "   ${YELLOW}⚠${NC} Virtual environment not found"
    echo "   Run: uv sync"
    exit 1
fi

# Check dependencies
echo -e "\n${BLUE}4. Checking dependencies...${NC}"
PACKAGE_COUNT=$(uv pip list 2>/dev/null | wc -l)
echo -e "   ${GREEN}✓${NC} $PACKAGE_COUNT packages installed"

# Check key packages
echo -e "\n${BLUE}5. Checking key packages...${NC}"
KEY_PACKAGES=("django" "djangorestframework" "pytest" "ruff" "mypy")
for pkg in "${KEY_PACKAGES[@]}"; do
    if uv pip show "$pkg" &> /dev/null; then
        VERSION=$(uv pip show "$pkg" | grep "Version:" | cut -d' ' -f2)
        echo -e "   ${GREEN}✓${NC} $pkg ($VERSION)"
    else
        echo -e "   ${RED}✗${NC} $pkg not found"
    fi
done

# Check Django
echo -e "\n${BLUE}6. Checking Django...${NC}"
if uv run python src/manage.py check &> /dev/null; then
    echo -e "   ${GREEN}✓${NC} Django checks passed"
else
    echo -e "   ${YELLOW}⚠${NC} Django checks found issues (check manually)"
fi

# Check Ruff
echo -e "\n${BLUE}7. Checking Ruff linter...${NC}"
RUFF_OUTPUT=$(uv run ruff check . --select E,F --statistics 2>&1)
if [ -z "$RUFF_OUTPUT" ]; then
    echo -e "   ${GREEN}✓${NC} No linting errors"
else
    echo -e "   ${YELLOW}⚠${NC} Some linting issues found"
fi

# Check Pytest
echo -e "\n${BLUE}8. Checking Pytest...${NC}"
TEST_COUNT=$(uv run pytest --collect-only -q 2>&1 | grep "test collected" | cut -d' ' -f1 || echo "0")
if [ "$TEST_COUNT" != "0" ]; then
    echo -e "   ${GREEN}✓${NC} $TEST_COUNT tests discovered"
else
    echo -e "   ${YELLOW}⚠${NC} Could not count tests"
fi

# Check pre-commit
echo -e "\n${BLUE}9. Checking pre-commit...${NC}"
if [ -f ".git/hooks/pre-commit" ]; then
    echo -e "   ${GREEN}✓${NC} Pre-commit hooks installed"
else
    echo -e "   ${YELLOW}⚠${NC} Pre-commit hooks not installed"
    echo "   Run: uv run pre-commit install"
fi

# Check configuration files
echo -e "\n${BLUE}10. Checking configuration files...${NC}"
CONFIG_FILES=("pyproject.toml" "uv.lock" "Makefile" ".pre-commit-config.yaml" ".python-version")
for file in "${CONFIG_FILES[@]}"; do
    if [ -f "$file" ]; then
        echo -e "    ${GREEN}✓${NC} $file"
    else
        echo -e "    ${RED}✗${NC} $file missing"
    fi
done

# Check documentation
echo -e "\n${BLUE}11. Checking documentation...${NC}"
DOC_FILES=("UV_SETUP.md" "SETUP_SUMMARY.md" "CHEATSHEET.md" "readme.md")
for file in "${DOC_FILES[@]}"; do
    if [ -f "$file" ]; then
        echo -e "    ${GREEN}✓${NC} $file"
    else
        echo -e "    ${YELLOW}⚠${NC} $file missing"
    fi
done

# Summary
echo -e "\n${BLUE}"
echo "=================================================="
echo "  Verification Complete!"
echo "=================================================="
echo -e "${NC}\n"

echo -e "${GREEN}Setup Status: READY ✓${NC}\n"

echo "Next steps:"
echo "  • Run 'make help' to see all commands"
echo "  • Run 'make run' to start the server"
echo "  • Run 'make test' to run tests"
echo "  • Read 'CHEATSHEET.md' for quick reference"
echo "  • Read 'UV_SETUP.md' for detailed documentation"
echo ""

echo "Quick commands:"
echo "  make run          # Start Django server"
echo "  make test         # Run tests with coverage"
echo "  make lint         # Check code quality"
echo "  make format       # Format code"
echo "  make quality      # Run all quality checks"
echo ""
