FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY ./src .

# Expose the port the app runs on
EXPOSE 5000

# Command to run the app 
#CMD ["python", "app.py"]  
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app", "-w", "4", "--timeout", "60"]