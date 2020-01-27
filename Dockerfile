FROM debian:latest

RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/* \
    && localedef -i fr_FR -c -f UTF-8 -A /usr/share/locale/locale.alias fr_FR.UTF-8 \
    && apt-get update && apt-get install -y pelican apache2
ENV LANG fr_FR.utf8

COPY . /srv/app
WORKDIR /srv/app

RUN pelican -s publishconf.py
RUN mv public/* /var/www/html/

EXPOSE 80
CMD apachectl -D FOREGROUND -e info 
