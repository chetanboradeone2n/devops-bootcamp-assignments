FROM python:3.9-alpine AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM python:3.9-alpine AS runtime
WORKDIR /app
COPY --from=builder /install /usr/local
COPY . .
ENTRYPOINT ["python"]
CMD ["main.py"]