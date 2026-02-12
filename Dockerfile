# BUILD 
FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .

RUN pip install --prefix=/install -r requirements.txt

# RUN
FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /install /usr/local
COPY . .
ENTRYPOINT ["python", "app.py"]

