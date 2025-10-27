# Use official Python image
FROM python:3.11-slim

RUN apt-get update

WORKDIR /app
# Set working directory for the CTFUser
RUN useradd -m ctfuser && chown -R ctfuser:ctfuser /app

# Running as CTFUser
USER ctfuser

# Copy requirements and install
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8080

# Command to run the app
CMD ["python", "app.py"]
