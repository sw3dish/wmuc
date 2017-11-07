FROM ubuntu:16.04

# install python3
RUN apt-get update && apt-get install -y build-essential \
    python3 \
    python3-dev \
    python3-pip

WORKDIR /srv/www

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt --upgrade pip

RUN mkdir -p /srv/uwsgi
COPY uwsgi.ini /srv/uwsgi
