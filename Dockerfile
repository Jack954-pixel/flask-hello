# Use official Python image
FROM python:3.10.x

# Set working directory inside container
WORKDIR /app

# Copy all files to the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 5000 for Flask
EXPOSE 8080

# Start the application using Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
