# Use Python as the base
FROM python:3.9-slim

# This creates a folder CALLED 'app' inside the container image
WORKDIR /app

# Copy your requirements.txt from your Git repo into the container
COPY requirements.txt .

# Install Flask and Gunicorn
RUN pip install --no-cache-dir -r requirements.txt

# Copy your templates, static, sqlite.db, and python files into the container
COPY . .

# Tell Google Cloud to use port 8080
EXPOSE 8080

# Start the site using Gunicorn
# (Assumes your file is main.py and the Flask line is app = Flask(__name__))
CMD ["gunicorn", "--bind", ":8080", "--workers", "1", "--threads", "8", "main:app"]
