FROM python:3.10-slim-bullseye

WORKDIR /app

RUN apt-get update && apt-get upgrade -y && \
    apt-get install --no-install-recommends -y \
    bash \
    curl \
    git \
    libffi-dev \
    libjpeg-dev \
    libwebp-dev \
    neofetch \
    libpq-dev \
    libcurl4-openssl-dev \
    libxml2-dev \
    libxslt1-dev \
    python3-dev \
    gcc \
    sqlite3 \
    libsqlite3-dev \
    ffmpeg \
    libopus0 \
    libopus-dev \
    wget \
    unzip \
    openssl \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives /tmp

COPY requirements.txt .
RUN pip3 install --upgrade pip setuptools wheel
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "-m", "FallenRobot"]
