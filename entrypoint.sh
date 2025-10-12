#!/bin/sh

set -e

if [ -z ${POSTGRES_DB+x} ]; then
  echo "SQLite will be used.";
else
  wait-for-it -s "$POSTGRES_HOST:$POSTGRES_PORT" -t 60
fi

# Apply database migrations
echo "Running Django migrations..."
python manage.py migrate --noinput

# Collect static files (ignore failure if not configured)
echo "Collecting static files..."
python manage.py collectstatic --noinput || true

echo "Starting application..."
exec "$@"
