# Base image
FROM python:3.12

# Set working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port your application runs on
EXPOSE 8000

# Command to run the application
CMD ["python", "main.py", "-r"]