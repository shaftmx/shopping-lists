FROM python:2

COPY ./requirements.txt /
RUN pip install -r /requirements.txt

COPY ./shopping-lists/project/settings/local.py /local.py.template
COPY ./shopping-lists /shopping-lists
COPY ./docker/entrypoint /entrypoint

ENTRYPOINT ["/entrypoint"]

