FROM python:3.10-slim-bullseye

ARG CACHE_BUST=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    git curl wget gcc libpq-dev \
    libffi-dev libssl-dev \
    ffmpeg libopus0 libopus-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "-m", "FallenRobot"]
