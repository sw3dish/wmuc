FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
    icecast2

COPY icecast.xml /etc/icecast2/icecast.xml
COPY icecast2 /etc/default/icecast2

# TODO: Get logs passed on to the Vagrant box
CMD icecast2 -c /etc/icecast2/icecast.xml
