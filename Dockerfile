# ==============================
# Stage 1: Build dependencies
# ==============================
FROM python:3.11-slim AS builder

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install UV
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Create and set the working directory
WORKDIR /app

# Copy dependency files
COPY pyproject.toml .
COPY uv.lock* .

# Install dependencies with UV
RUN uv sync --frozen --no-dev --no-editable

# ==============================
# Stage 2: Final runtime image
# ==============================
FROM python:3.11-slim

# Install runtime utilities
RUN apt-get update && apt-get install -y --no-install-recommends dumb-init && rm -rf /var/lib/apt/lists/*

# Install UV in final image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH="/app/src:$PYTHONPATH"

# Create and set the working directory
WORKDIR /app

# Copy virtual environment from builder
COPY --from=builder /app/.venv /app/.venv

# Copy the Django project code
COPY . /app

# Ensure script is executable and set permissions for the non-root user
# RUN chmod +x /app/entrypoint.sh

#ENTRYPOINT ["dumb-init", "/app/entrypoint.sh"]
