
# Use official Python image
FROM python:3.12-slim

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies needed for psycopg
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Create project directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files
COPY . /app/

# Expose port
EXPOSE 8000

# Run server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
