# ----------- Stage 1: Build Environment -----------
FROM python:3.13.3-slim as builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y gcc libpq-dev && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install node dependencies (if needed)
# RUN apt-get install -y nodejs npm
# RUN npm install

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Run database migrations
# RUN python manage.py migrate --noinput

# Collect static files
# RUN python manage.py collectstatic --noinput

# ----------- Stage 2: Production Image -----------
FROM python:3.13.3-slim

WORKDIR /app

# Install runtime dependencies
RUN apt-get update && apt-get install -y libpq-dev && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy installed packages from builder
COPY --from=builder /usr/local /usr/local

# Copy app source code
COPY --from=builder /app /app

# Set environment variable to let Django know it's in production
ENV DJANGO_SETTINGS_MODULE=LittleLemon.settings

# Expose port
EXPOSE 8000

# Run app with Uvicorn
CMD ["sh", "-c", "python manage.py migrate --noinput && python manage.py collectstatic --noinput && uvicorn LittleLemon.asgi:application --host 0.0.0.0 --port 8000"]
