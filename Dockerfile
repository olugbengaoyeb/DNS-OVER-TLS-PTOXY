# Docker image to pull from
FROM python:3.8-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3-openssl \
    && rm -rf /var/lib/apt/lists/*

# Copy proxy script
COPY proxy.py /app/proxy.py

# Run proxy
CMD ["python", "/app/proxy.py"]
#This will start the DNS proxy and bind it to port 53 on the host machine.
