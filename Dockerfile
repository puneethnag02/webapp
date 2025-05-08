# Use official Python image
FROM python:3.9-slim

# Set work directory
WORKDIR /app

# Copy files
COPY requirements.txt .
RUN pip install --no-cache-dir  -r requirements.txt
COPY . .

# Run app
CMD ["python", "app.py"]

