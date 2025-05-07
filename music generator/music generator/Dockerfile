# Start from an official Python 3.10 base image
FROM python:3.10-slim

# Set environment variables to prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app/

# Ensure pip is upgraded (python3 is available by default)
RUN python3 -m pip install --upgrade pip

# Install the required Python packages
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# Specify the command to run your app
CMD ["python3", "app.py"]

