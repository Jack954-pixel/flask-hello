# Use an official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy all files to the container
COPY . /app

# Install dependencies
RUN pip3 install -r requirements.txt

# Run the application
CMD [ "flask", "run", "--host=0.0.0.0"]
