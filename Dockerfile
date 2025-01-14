FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y \
    gcc \
    libmariadb-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 5000

CMD ["python", "run.py"]
