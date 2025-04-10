FROM python:3.13.3-alpine

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir --break-system-packages -r requirements.txt

RUN echo "America/Belem" > /etc/timezone

COPY . .