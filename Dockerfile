FROM python:3.9  
# Base image with Python 3.9

WORKDIR /app

# Install Flask dependency
RUN pip install Flask

COPY . .  
# Copy application code to working directory

CMD ["python", "app.py"]  # Start the application
