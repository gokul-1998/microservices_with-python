FROM python:3.10-slim-bullseye

RUN apt-get update\
    && apt-get install -y --no-install-recommends \
    --no-install-suggests \
    build-essential default-libmysqlclient-dev\
    && pip install --no-cache-dir --upgrade pip\
    && apt-get install -y python3-dev default-libmysqlclient-dev build-essential pkg-config

WORKDIR /app

COPY ./requirements.txt /app
RUN pip install --no-cache-dir -r /app/requirements.txt -v && \
    /bin/bash

COPY . /app

EXPOSE 5000

CMD [ "python3", "server.py"]