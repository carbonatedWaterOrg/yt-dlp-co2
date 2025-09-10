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

# Non-root user for security
RUN addgroup -g 1000 appuser && \
    adduser -u 1000 -G appuser -D appuser

# Create directories and set ownership
RUN mkdir -p /app/downloads /app/config && \
    chown -R appuser:appuser /app

# Create entrypoint script to handle permissions at runtime
RUN echo '#!/bin/sh' > /app/entrypoint.sh && \
    echo 'mkdir -p /app/downloads /app/config' >> /app/entrypoint.sh && \
    echo 'chown -R appuser:appuser /app/downloads /app/config 2>/dev/null || true' >> /app/entrypoint.sh && \
    echo 'exec "$@"' >> /app/entrypoint.sh && \
    chmod +x /app/entrypoint.sh && \
    chown appuser:appuser /app/entrypoint.sh

USER appuser

EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]