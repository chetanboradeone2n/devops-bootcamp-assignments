# Builder stage
FROM python:3.9-alpine as builder
RUN apk add --no-cache gcc musl-dev postgresql-dev
WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Runtime stage
FROM python:3.9-alpine
RUN apk add --no-cache libpq
COPY --from=builder /root/.local /root/.local
ENV PATH="/root/.local/bin:$PATH"
WORKDIR /app
COPY . .
ENTRYPOINT [ "python" ]
CMD ["main.py"]