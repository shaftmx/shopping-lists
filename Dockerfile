FROM python:2

RUN apt-get update && apt-get install -y gettext-base && apt-get clean
COPY ./requirements.txt /
RUN pip install -r /requirements.txt

COPY ./shopping-lists/project/settings/local.py /local.py.template
COPY ./shopping-lists /shopping-lists
COPY ./docker/entrypoint /entrypoint

ENTRYPOINT ["/entrypoint"]

