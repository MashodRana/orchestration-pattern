# Use official Python image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Make run_worker.sh executable
RUN chmod +x run_worker.sh

# Default command to run the Celery worker
CMD ["./run_worker.sh"]