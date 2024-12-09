# Use the latest CPython image as the base
FROM python:latest

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Run the specified command within the container
CMD ["python3", "inventory.py"]

