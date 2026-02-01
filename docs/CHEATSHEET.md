# UV & Development Commands Cheat Sheet

## 🚀 Quick Reference

### Essential Commands

```bash
# Get started
./quickstart.sh              # Quick setup and start
make help                    # Show all commands
make dev-setup              # Full development setup

# Daily development
make run                    # Start Django server
make test                   # Run tests
make lint                   # Check code quality
make format                 # Format code

# Quality checks (run before commit)
make quality                # Run all quality checks
make ci                     # Run full CI checks locally
```

## 📦 UV Commands

### Installation & Setup

```bash
# Install UV
curl -LsSf https://astral.sh/uv/install.sh | sh

# Sync dependencies (install/update)
uv sync

# Install only production deps
uv sync --no-dev

# Update dependencies
uv lock --upgrade && uv sync
```

### Package Management

```bash
# Add packages
uv add django-extensions              # Production
uv add --dev pytest-mock             # Development

# Remove packages
uv remove package-name

# Show installed packages
uv pip list

# Show dependency tree
uv pip tree

# Show outdated packages
uv pip list --outdated
```

### Running Commands

```bash
# Run Python scripts
uv run python script.py

# Django management
uv run python manage.py <command>

# Run any installed tool
uv run pytest
uv run ruff check .
uv run mypy .
```

## 🎯 Make Commands (Shortcuts)

### Development

```bash
make run                    # python manage.py runserver
make shell                  # python manage.py shell
make migrate                # python manage.py migrate
make makemigrations         # python manage.py makemigrations
make createsuperuser        # python manage.py createsuperuser
make check                  # python manage.py check
```

### Code Quality

```bash
make lint                   # ruff check .
make lint-fix              # ruff check --fix .
make format                # ruff format .
make format-check          # ruff format --check .
make type-check            # mypy .
make pre-commit            # pre-commit run --all-files
make quality               # Run all quality checks
make audit                 # pip-audit (security check)
```

### Testing

```bash
make test                  # pytest with coverage
make test-cov             # pytest with detailed coverage
make test-fast            # pytest -n auto (parallel)
make test-unit            # pytest -m unit
make test-integration     # pytest -m integration
make test-verbose         # pytest -vv
make test-failed          # pytest --lf (last failed)
make coverage-report      # Open HTML coverage report
```

### Dependencies

```bash
make install              # Install production deps
make install-dev          # Install all deps + setup
make sync                 # Sync with lock file
make update               # Update all dependencies
make freeze               # Show installed packages
make tree                 # Show dependency tree
make show-outdated        # Show outdated packages
```

### Docker

```bash
make docker-build         # docker-compose build
make docker-up            # docker-compose up -d
make docker-down          # docker-compose down
make docker-logs          # docker-compose logs -f
make docker-shell         # docker-compose exec web bash
```

### Cleanup

```bash
make clean                # Remove cache files
make dev-reset            # Clean + fresh setup
```

## 🔍 Ruff Commands

```bash
# Linting
uv run ruff check .                    # Check all files
uv run ruff check --fix .              # Auto-fix issues
uv run ruff check --watch .            # Watch mode
uv run ruff check path/to/file.py      # Check specific file

# Formatting
uv run ruff format .                   # Format all files
uv run ruff format --check .           # Check formatting
uv run ruff format path/to/file.py     # Format specific file

# Rules
uv run ruff rule E501                  # Explain rule
uv run ruff check --select E,F .       # Check specific rules
```

## 🧪 Pytest Commands

```bash
# Basic
uv run pytest                          # Run all tests
uv run pytest -v                       # Verbose
uv run pytest -vv                      # Very verbose
uv run pytest -x                       # Stop on first failure
uv run pytest -s                       # Show print statements

# Specific tests
uv run pytest path/to/test_file.py     # Specific file
uv run pytest path/to/test_file.py::TestClass::test_method  # Specific test

# Markers
uv run pytest -m unit                  # Run unit tests
uv run pytest -m "not slow"            # Skip slow tests
uv run pytest -m integration           # Run integration tests

# Coverage
uv run pytest --cov                    # With coverage
uv run pytest --cov --cov-report=html  # HTML report
uv run pytest --cov --cov-report=term-missing  # Show missing lines

# Parallel
uv run pytest -n auto                  # Auto-detect CPUs
uv run pytest -n 4                     # Use 4 CPUs

# Rerun
uv run pytest --lf                     # Last failed
uv run pytest --ff                     # Failed first
```

## 🛡️ Type Checking (Mypy)

```bash
uv run mypy .                          # Check all files
uv run mypy path/to/file.py            # Check specific file
uv run mypy --strict .                 # Strict mode
uv run mypy --show-error-codes .       # Show error codes
```

## 🎣 Pre-commit

```bash
# Setup
uv run pre-commit install              # Install hooks
uv run pre-commit uninstall            # Remove hooks

# Run
uv run pre-commit run                  # Run on staged files
uv run pre-commit run --all-files      # Run on all files
uv run pre-commit run ruff             # Run specific hook

# Maintenance
uv run pre-commit autoupdate           # Update hook versions
uv run pre-commit clean                # Clean cache
```

## 🐳 Docker

```bash
# Build
docker-compose build
docker-compose build --no-cache

# Run
docker-compose up                      # Foreground
docker-compose up -d                   # Background
docker-compose up --build              # Build and run

# Stop
docker-compose down                    # Stop containers
docker-compose down -v                 # Stop and remove volumes

# Logs
docker-compose logs                    # All logs
docker-compose logs -f                 # Follow logs
docker-compose logs web                # Service logs

# Execute
docker-compose exec web bash           # Shell
docker-compose exec web python manage.py migrate
```

## 🔧 Django Management

```bash
# Database
uv run python manage.py migrate
uv run python manage.py makemigrations
uv run python manage.py showmigrations
uv run python manage.py sqlmigrate app_name 0001

# Users
uv run python manage.py createsuperuser
uv run python manage.py changepassword username

# Shell
uv run python manage.py shell
uv run python manage.py dbshell

# Static files
uv run python manage.py collectstatic
uv run python manage.py findstatic file.css

# Other
uv run python manage.py check
uv run python manage.py check --deploy
uv run python manage.py showurls  # If django-extensions installed
```

## 🔒 Security

```bash
# Dependency audit
uv run pip-audit
uv run pip-audit --fix

# Code scanning
uv run bandit -r . -c pyproject.toml
uv run bandit -r . -f json -o report.json
```

## 📊 Coverage

```bash
# Run with coverage
uv run pytest --cov

# Generate reports
uv run coverage html                   # HTML report
uv run coverage xml                    # XML report
uv run coverage report                 # Terminal report
uv run coverage report --show-missing  # Show missing lines

# Open HTML report
open htmlcov/index.html               # macOS
xdg-open htmlcov/index.html          # Linux
```

## 🎓 Git Workflow with Pre-commit

```bash
# Setup (once)
uv run pre-commit install

# Normal workflow
git add .
git commit -m "message"               # Pre-commit runs automatically

# Skip pre-commit (not recommended)
git commit -m "message" --no-verify

# Manual pre-commit check before commit
uv run pre-commit run --all-files
# OR
make pre-commit
```

## 💡 Tips

1. **Use `make` commands** - They're shorter and easier to remember
2. **Always use `uv run`** - Ensures you're using the project environment
3. **Run `make quality`** before committing - Catches issues early
4. **Use `make test-fast`** - For quick feedback during development
5. **Check `make help`** - When you forget a command

## 🆘 Troubleshooting

```bash
# UV not found
export PATH="$HOME/.cargo/bin:$PATH"

# Dependency conflicts
rm uv.lock && uv sync

# Virtual environment issues
rm -rf .venv && uv sync

# Cache issues
make clean && uv sync

# Pre-commit issues
uv run pre-commit clean
uv run pre-commit install

# Test issues
rm -rf .pytest_cache
uv run pytest --cache-clear
```

## 📁 Important Files

```
pyproject.toml              # All configuration
uv.lock                     # Dependency lock file
Makefile                    # Command shortcuts
.pre-commit-config.yaml     # Pre-commit hooks
.python-version             # Python version
.github/workflows/ci.yml    # CI pipeline
```

## 🎯 Before Every Commit

```bash
make quality                # Or manually:
make lint                   # Check linting
make format-check           # Check formatting
make type-check             # Check types
make test                   # Run tests
```

## 🚀 Before Every Push

```bash
make ci                     # Run full CI checks locally
```

---

**Print this and keep it handy! 📄**
