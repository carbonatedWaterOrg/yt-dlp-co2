FROM python:3.13.7-alpine

WORKDIR /app

# Install system dependencies for yt-dlp
RUN apk add --no-cache \
    ffmpeg \
    ca-certificates

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./app/
COPY index.html ./
COPY static/ ./static/
COPY README.md ./README.md

# Create directories
RUN mkdir -p /app/downloads /app/config

# Non-root user for security
RUN addgroup -g 1000 appuser && \
    adduser -u 1000 -G appuser -D appuser && \
    chown -R appuser:appuser /app

USER appuser

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]