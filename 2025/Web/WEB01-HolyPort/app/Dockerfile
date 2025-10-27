# The base Docker file for the initial web CTF for Deadface 2025
# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy challenge files
COPY . .

# Create a non-root user
RUN useradd -m ctfuser
# Change ownership to ctfuser
RUN chown -R ctfuser:ctfuser /app
# Switch to non-root user
USER ctfuser

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Use build arg to dynamically set EXPOSE
ARG LPORT=5000
ENV LPORT=${LPORT}
ARG FLASK_ENV
ENV FLASK_ENV=${FLASK_ENV}
ARG PYTHONDONTWRITEBYTECODE
ENV PYTHONDONTWRITEBYTECODE=${PYTHONDONTWRITEBYTECODE}
ARG PYTHONUNBUFFERED
ENV PYTHONUNBUFFERED=${PYTHONUNBUFFERED}

# Expose the configured port (metadata)
EXPOSE ${LPORT}

# Run the challenge
CMD ["python", "app.py"]

