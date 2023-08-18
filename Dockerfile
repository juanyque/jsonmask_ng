ARG PYTHON_VERSION=3.7
FROM python:$PYTHON_VERSION-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update
RUN apk add \
  build-base \
  gcc \
  libpq libpq-dev \
  python3-dev \
  libffi-dev \
  graphviz \
  git

# RUN mkdir -p /root/.ssh
# RUN chmod 700 /root/.ssh/

RUN mkdir -p /app/.venv
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install wheel setuptools cmake twine --upgrade

# Install poetry
ARG POETRY_VERSION=1.5.1
RUN pip install poetry==$POETRY_VERSION

#TODO: Use requirements instead poetry and make?
# COPY ./requirements.txt .
# RUN pip install -r requirements.txt

COPY . .
# ADD . .

RUN rm -r /app/.venv
# RUN poetry lock --no-update
RUN make all
