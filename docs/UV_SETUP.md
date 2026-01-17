# UV Setup Guide for Lottery Project

This project now uses [UV](https://github.com/astral-sh/uv) - an extremely fast Python package installer and resolver
written in Rust. UV replaces pip, pip-tools, virtualenv, and more.

## 🚀 Quick Start

### 1. Install UV

**macOS/Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**With pip (if you already have Python):**

```bash
pip install uv
```

### 2. Setup Development Environment

```bash
# Install all dependencies (including dev dependencies)
make install-dev

# Or manually:
uv sync
uv run pre-commit install
```

### 3. Run the Project

```bash
# Run migrations
make migrate

# Start development server
make run

# Or manually:
uv run python manage.py migrate
uv run python manage.py runserver
```

## 📋 Common Commands

All common tasks are available through the Makefile. Run `make help` to see all available commands.

### Development Workflow

```bash
make dev-setup          # Complete development setup
make run               # Start Django development server
make shell             # Start Django shell
```

### Code Quality

```bash
make lint              # Run linting
make lint-fix          # Run linting and auto-fix issues
make format            # Format code
make type-check        # Run type checking
make quality           # Run all quality checks
make pre-commit        # Run pre-commit hooks
```

### Testing

```bash
make test              # Run tests with coverage
make test-fast         # Run tests in parallel
make test-cov          # Run tests with detailed coverage
make coverage-report   # Open HTML coverage report
```

### Dependency Management

```bash
make install           # Install production dependencies
make install-dev       # Install all dependencies
make update            # Update all dependencies
make audit             # Security audit
```

### Django Management

```bash
make migrate           # Apply migrations
make makemigrations    # Create migrations
make createsuperuser   # Create superuser
make check             # Run Django checks
```

## 🔧 UV Command Reference

### Running Python Commands

```bash
# Run any Python command
uv run python script.py

# Run Django management commands
uv run python manage.py <command>

# Run pytest
uv run pytest

# Run any installed CLI tool
uv run ruff check .
```

### Managing Dependencies

```bash
# Add a new dependency
uv add django-extensions

# Add a dev dependency
uv add --dev pytest-mock

# Remove a dependency
uv remove django-extensions

# Update dependencies
uv lock --upgrade
uv sync

# Show installed packages
uv pip list

# Show dependency tree
uv pip tree
```

### Virtual Environment

UV automatically manages virtual environments for you. By default, it creates a `.venv` directory in your project.

```bash
# Sync dependencies (creates/updates .venv)
uv sync

# Run commands in the virtual environment
uv run python manage.py runserver

# Activate the virtual environment manually (if needed)
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```

## 🛠️ Project Structure

```
lottery/
├── pyproject.toml          # Project metadata and all tool configurations
├── uv.lock                 # Locked dependency versions (auto-generated)
├── .python-version         # Python version specification
├── Makefile               # Common development tasks
├── .pre-commit-config.yaml # Pre-commit hooks configuration
├── manage.py              # Django management script
└── ...
```

## 📦 Tool Configurations

All tool configurations are centralized in `pyproject.toml`:

- **Ruff**: Fast linter and formatter (replaces black, flake8, isort, etc.)
- **Pytest**: Test runner with coverage
- **Mypy**: Type checking
- **Coverage**: Code coverage reporting
- **Bandit**: Security issue detection

## 🔍 Code Quality Tools

### Ruff (Linting & Formatting)

Ruff is an extremely fast Python linter and formatter that replaces multiple tools:

- ✅ Replaces: Black, Flake8, isort, pyupgrade, and more
- ⚡ 10-100x faster than existing tools
- 🔧 Auto-fixes many issues

```bash
# Check for issues
uv run ruff check .

# Auto-fix issues
uv run ruff check --fix .

# Format code
uv run ruff format .
```

### Mypy (Type Checking)

Static type checker for Python:

```bash
uv run mypy .
```

### Pre-commit Hooks

Automatically run checks before each commit:

```bash
# Install hooks
uv run pre-commit install

# Run manually on all files
uv run pre-commit run --all-files
```

## 🧪 Testing

### Running Tests

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov

# Run in parallel (faster)
uv run pytest -n auto

# Run specific test file
uv run pytest lottery_event/tests/test_lottery_event_views.py

# Run specific test
uv run pytest lottery_event/tests/test_lottery_event_views.py::TestClassName::test_method
```

### Test Markers

```bash
# Run only unit tests
uv run pytest -m unit

# Run only integration tests
uv run pytest -m integration

# Skip slow tests
uv run pytest -m "not slow"
```

## 🐳 Docker

```bash
make docker-build      # Build Docker image
make docker-up         # Start containers
make docker-down       # Stop containers
make docker-logs       # View logs
make docker-shell      # Access container shell
```

## 🔒 Security

```bash
# Run security audit on dependencies
make audit

# Or manually:
uv run pip-audit

# Run bandit security checks (via pre-commit)
uv run bandit -r . -c pyproject.toml
```

## 💡 Tips and Best Practices

1. **Always use `uv run`** for running Python commands to ensure you're using the project's environment
2. **Use `make` commands** for common tasks - they're shorter and more memorable
3. **Run `make quality`** before committing to catch issues early
4. **Keep dependencies up to date** with `make update` regularly
5. **Use pre-commit hooks** to automatically check code quality on each commit

## 🆚 UV vs Traditional Tools

| Traditional                       | UV Equivalent                       |
|-----------------------------------|-------------------------------------|
| `pip install -r requirements.txt` | `uv sync`                           |
| `pip install package`             | `uv add package`                    |
| `pip install --dev package`       | `uv add --dev package`              |
| `pip freeze > requirements.txt`   | `uv lock` (automatic)               |
| `python manage.py runserver`      | `uv run python manage.py runserver` |
| `pytest`                          | `uv run pytest`                     |
| `source venv/bin/activate`        | Not needed! Use `uv run`            |

## 🚨 Troubleshooting

### UV not found

```bash
# Reinstall UV
curl -LsSf https://astral.sh/uv/install.sh | sh

# Add to PATH (if needed)
export PATH="$HOME/.cargo/bin:$PATH"
```

### Dependency conflicts

```bash
# Clear lock file and resync
rm uv.lock
uv sync
```

### Pre-commit issues

```bash
# Reinstall pre-commit hooks
uv run pre-commit uninstall
uv run pre-commit install
```

### Virtual environment issues

```bash
# Remove and recreate
rm -rf .venv
uv sync
```

## 📚 Additional Resources

- [UV Documentation](https://github.com/astral-sh/uv)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [Django Documentation](https://docs.djangoproject.com/)
- [Pytest Documentation](https://docs.pytest.org/)

## 🎯 Migration from requirements.txt

The old `requirements.txt` is no longer needed as dependencies are now managed in `pyproject.toml`. The file is kept for
reference but UV uses `pyproject.toml` and `uv.lock` instead.

If you need to regenerate requirements.txt for deployment:

```bash
uv pip compile pyproject.toml -o requirements.txt
```
