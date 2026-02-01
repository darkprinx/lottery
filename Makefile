.PHONY: help install install-dev sync update clean lint format type-check test test-cov test-fast run migrate makemigrations shell pre-commit audit docker-build docker-up docker-down

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-20s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

# ============================================================================
# Installation & Setup
# ============================================================================

install: ## Install production dependencies with UV
	uv sync --no-dev

install-dev: ## Install all dependencies including dev dependencies
	uv sync
	uv run pre-commit install

sync: ## Sync dependencies with lock file
	uv sync

update: ## Update dependencies
	uv lock --upgrade
	uv sync

clean: ## Clean up cached files and build artifacts
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.coverage" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	rm -rf htmlcov/ .coverage coverage.xml dist/ build/

# ============================================================================
# Code Quality
# ============================================================================

lint: ## Run linting with ruff
	uv run ruff check src

lint-fix: ## Run linting with ruff and fix issues
	uv run ruff check --fix src

format: ## Format code with ruff
	uv run ruff format src

format-check: ## Check code formatting without making changes
	uv run ruff format --check src

type-check: ## Run type checking with mypy
	uv run mypy src

pre-commit: ## Run pre-commit hooks on all files
	uv run pre-commit run --all-files

audit: ## Run security audit on dependencies
	uv run pip-audit

quality: pre-commit type-check ## Run all code quality checks

# ============================================================================
# Testing
# ============================================================================

test: ## Run tests with coverage
	uv run pytest

test-cov: ## Run tests with detailed coverage report
	uv run pytest --cov-report=term-missing --cov-report=html

test-fast: ## Run tests in parallel (faster)
	uv run pytest -n auto

test-unit: ## Run only unit tests
	uv run pytest -m unit

test-integration: ## Run only integration tests
	uv run pytest -m integration

test-verbose: ## Run tests with verbose output
	uv run pytest -vv

test-failed: ## Run only failed tests from last run
	uv run pytest --lf

coverage-report: ## Open HTML coverage report in browser
	@echo "Opening coverage report..."
	@python -m webbrowser htmlcov/index.html || open htmlcov/index.html || xdg-open htmlcov/index.html

# ============================================================================
# Django Management
# ============================================================================

run: ## Run Django development server
	uv run python src/manage.py runserver

migrate: ## Apply database migrations
	uv run python src/manage.py migrate

makemigrations: ## Create new database migrations
	uv run python src/manage.py makemigrations

shell: ## Start Django shell
	uv run python src/manage.py shell

shell-plus: ## Start Django shell with ipython
	uv run python src/manage.py shell

createsuperuser: ## Create Django superuser
	uv run python src/manage.py createsuperuser

collectstatic: ## Collect static files
	uv run python src/manage.py collectstatic --noinput

check: ## Run Django system checks
	uv run python src/manage.py check

showmigrations: ## Show migration status
	uv run python src/manage.py showmigrations

# ============================================================================
# Docker
# ============================================================================

docker-build: ## Build Docker image
	docker-compose build

docker-up: ## Start Docker containers
	docker-compose up -d

docker-down: ## Stop Docker containers
	docker-compose down

docker-logs: ## Show Docker logs
	docker-compose logs -f

docker-shell: ## Access Docker container shell
	docker-compose exec web bash

# ============================================================================
# Development Workflow
# ============================================================================

dev-setup: install-dev migrate ## Complete development setup
	@echo "Development environment is ready!"
	@echo "Run 'make run' to start the development server"

dev-reset: clean dev-setup ## Reset development environment

ci: quality test ## Run CI checks locally (linting, formatting, type checking, tests)

release-check: ci audit ## Run all checks before release

# ============================================================================
# Utilities
# ============================================================================

freeze: ## Show installed packages
	uv pip list

tree: ## Show dependency tree
	uv pip tree

show-outdated: ## Show outdated packages
	uv pip list --outdated
