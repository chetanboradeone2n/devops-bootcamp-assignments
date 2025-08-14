# This is the Builder Stage
FROM python:3.9-slim as builder
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /build
COPY requirements.txt .
RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install --no-cache-dir wheel && \
    /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# This is the Runtime Stage
FROM python:3.9-slim
COPY --from=builder /opt/venv /opt/venv
RUN apt-get update && apt-get install -y \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*
ENV PATH="/opt/venv/bin:$PATH"
WORKDIR /app
COPY . .
EXPOSE 5000
ENV PYTHONUNBUFFERED=1
CMD ["python", "main.py"]