#!/bin/bash
set -e  # Exit on any error

echo "🚀 Starting Django build process on Vercel..."

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Create necessary directories
mkdir -p staticfiles

# Run Django migrations
echo "🗃️ Running database migrations..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

echo "✅ Build process completed successfully!"