FROM nginx:1.12.1
LABEL maintainer="sw3dish (Colin Burr)"

RUN rm /etc/nginx/conf.d/default.conf
COPY wmuc.conf /etc/nginx/conf.d/wmuc.conf

VOLUME /srv/www
WORKDIR /srv/www
