# Lottery Project

## 🎯 Overview

A Django-based lottery event management system where users can participate in daily lottery events and purchase ballots.

### Functional Requirements & Assumptions

```
● Only one event can be created each day.
● Users can register for lottery events as participants.
● Lottery participants will be able to buy as many lottery ballots as possible which is not
  closed yet.
● Each day at midnight the lottery event will be closed and a random lottery-winning ballot
  will be selected from all the participants.
● All users will be able to check the winning ballot for any specific date.
```

### Additional Features

```
● The winner will be notified via email.
● Users have to pay per lottery ballot submission.
```

---

## 🚀 Quick Start

### Option 1: Using UV (Recommended for Development)

This project uses [UV](https://github.com/astral-sh/uv) for fast dependency management. All Django code is organized in
the `src/` folder.

#### Initial Setup

```bash
# Install UV (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Run the automated setup script
./scripts/setup_uv.sh

# Or manually:
uv sync                               # Install dependencies
uv run pre-commit install             # Setup pre-commit hooks
uv run python src/manage.py migrate   # Run migrations
uv run python src/manage.py runserver # Start server
```

#### Daily Development

```bash
make help          # See all available commands
make run           # Start development server
make test          # Run tests
make lint          # Check code quality
make format        # Format code
```

```bash
make help          # See all available commands
make run           # Start development server
make test          # Run tests
make lint          # Check code quality
make format        # Format code
```

**For detailed UV setup and usage, see [UV_SETUP.md](docs/UV_SETUP.md)**

### Option 2: Using Docker

Go to the project root folder **lottery** and run:

```bash
docker-compose up --build
```

The app will run on **0.0.0.0:8081**

Or with Make:

```bash
make docker-up     # Start containers
make docker-down   # Stop containers
make docker-logs   # View logs
```

---

## 📋 Development Tools

This project uses modern Python tooling:

- **[UV](https://github.com/astral-sh/uv)**: Ultra-fast package installer and resolver
- **[Ruff](https://docs.astral.sh/ruff/)**: Fast linter and formatter (replaces black, flake8, isort)
- **[Pytest](https://docs.pytest.org/)**: Testing framework with coverage
- **[Mypy](https://mypy-lang.org/)**: Static type checking
- **[Pre-commit](https://pre-commit.com/)**: Git hooks for code quality

### Pre-commit Hooks

To enable automatic code quality checks locally before each commit:

```bash
# Install pre-commit hooks (done automatically by make install-dev)
uv run pre-commit install

# Run on all files manually
uv run pre-commit run --all-files

# Or use make
make pre-commit
```

The configured hooks will run:

- Ruff (linting and formatting)
- Type checking with Mypy
- Security checks with Bandit
- File hygiene checks

---

## 🧪 Testing

```bash
# Run all tests
make test

# Run tests with coverage report
make test-cov

# Run tests in parallel (faster)
make test-fast

# Run specific tests
uv run pytest lottery_event/tests/test_lottery_event_views.py

# Open coverage report in browser
make coverage-report
```

---

## 📦 Dependency Management

### Adding Dependencies

```bash
# Add production dependency
uv add package-name

# Add development dependency
uv add --dev package-name

# Update all dependencies
make update
```

### Security Audit

```bash
make audit
```

---

## 🔧 Common Commands

| Task               | Command                |
|--------------------|------------------------|
| Start server       | `make run`             |
| Run tests          | `make test`            |
| Check code quality | `make quality`         |
| Format code        | `make format`          |
| Run migrations     | `make migrate`         |
| Create migrations  | `make makemigrations`  |
| Django shell       | `make shell`           |
| Create superuser   | `make createsuperuser` |
| See all commands   | `make help`            |

---

## 📁 Project Structure

```
lottery/
├── pyproject.toml              # Project config & dependencies
├── uv.lock                     # Locked dependency versions
├── Makefile                    # Development commands
├── .pre-commit-config.yaml     # Pre-commit hooks
├── manage.py                   # Django management
├── core/                       # Django settings
├── lottery_event/              # Lottery event app
├── payment/                    # Payment app
├── user/                       # User management app
└── utils/                      # Shared utilities
```

---

## 🔄 Migrating from pip to UV

If you're coming from the old pip-based setup:

```bash
./migrate_to_uv.sh
```

This will:

- Install UV if needed
- Install all dependencies
- Compare old and new setups
- Run tests to verify everything works

---

## 📚 Documentation

- **[UV_SETUP.md](docs/UV_SETUP.md)**: Complete UV setup and usage guide
- **[readme-doc.pdf](readme-doc.pdf)**: Full project documentation

---

## 🐳 Docker

```bash
# Build and start
make docker-build
make docker-up

# View logs
make docker-logs

# Stop containers
make docker-down
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run quality checks: `make ci`
5. Submit a pull request

---

## 📝 License

See project documentation for license information.
