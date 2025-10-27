# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy app files
COPY . .

# Create a non-root user
RUN useradd -m ctfuser
# Change ownership to ctfuser
RUN chown -R ctfuser:ctfuser /app
# Switch to non-root user
USER ctfuser

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Load environment variables at runtime (Flask reads from .env)
RUN pip install python-dotenv

# Use build arg to dynamically set EXPOSE
ARG LPORT=5000
ENV LPORT=${LPORT}

# Expose the configured port (metadata)
EXPOSE ${LPORT}

# Run the Flask app
CMD ["python", "app.py"]
