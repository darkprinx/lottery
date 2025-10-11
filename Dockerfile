# ==============================
# Stage 1: Build dependencies
# ==============================
FROM python:3.11-slim AS builder

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Create and set the working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r ./requirements.txt

# ==============================
# Stage 2: Final runtime image
# ==============================
FROM python:3.11-slim

# Install runtime utilities
RUN apt-get update && apt-get install -y --no-install-recommends dumb-init && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Copy installed dependencies from builder stage
COPY --from=builder /install /usr/local

# Copy the Django project code
COPY . /app

# Ensure script is executable and set permissions for the non-root user
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["dumb-init", "/app/entrypoint.sh"]