FROM python:3.7-alpine

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
RUN pip install poetry==1.5.1

#TODO: Use requirements instead poetry and make?
# COPY ./requirements.txt .
# RUN pip install -r requirements.txt

# COPY . /app 
ADD . .

# RUN poetry lock --no-update

RUN make all
