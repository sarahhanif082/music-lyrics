# Start from an official Python 3.10 base image
FROM python:3.10-slim

# Update and install dependencies (e.g., python3.10 and distutils)
RUN apt-get update && apt-get install -y python3.10 python3.10-distutils

# Ensure pip is installed and upgraded
RUN python3.10 -m ensurepip --upgrade

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install dependencies from requirements.txt
RUN python3.10 -m pip install --no-cache-dir -r requirements.txt

# Specify the command to run your app
CMD ["python3.10", "app.py"]
