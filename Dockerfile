# Use a lightweight Python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency list and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Python source code
COPY Python_code/ ./Python_code/

# Copy frontend files (HTML, CSS, JS)
COPY Website/ ./Website/

# Expose the Flask port
EXPOSE 5000

# Run the Flask app
CMD ["python", "Python_code/API.py"]
