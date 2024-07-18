# Dockerfile

# pull the official docker image
FROM python:3.11.1-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*  \
    libpq-dev


# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt .
RUN pip install psycopg2
RUN pip install sqlparse
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project
COPY . .