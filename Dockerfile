FROM python:2

RUN apt-get update && apt-get install -y gettext-base nginx && apt-get clean
RUN unlink /etc/nginx/sites-enabled/default
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./docker/config/nginx.conf.template /opt/
COPY ./docker/config/vhost.conf.template /opt/

COPY ./shopping-lists/project/settings/local.py /local.py.template
COPY ./shopping-lists /shopping-lists
COPY ./docker/entrypoint /entrypoint

ENTRYPOINT ["/entrypoint"]

