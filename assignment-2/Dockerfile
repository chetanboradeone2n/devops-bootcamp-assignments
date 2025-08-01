# Stage 1: Builder
FROM python:3.11-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --user -r requirements.txt

# Stage 2: Final Runtime Image
FROM python:3.11-slim

ENV PATH=/root/.local/bin:$PATH

WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY --from=builder /app /app
COPY app.py .

EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]

