FROM python:3.10.6-alpine3.16
LABEL maintainer="nathan"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
# COPY ./requirements.txt /app/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    # TO INSTALL psycopg2 package, dependencies needed
    apk add --update --no-cache postgresql-client && \
    #"""temperary folder for tempy dependencies packages use to \
    #intall psycopg2 but are not used for application running"""
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \ 
    /py/bin/pip install -r /tmp/requirements.txt && \
    # /py/bin/pip install -r /app/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    # """deleting the temperary folder as these packages are \ 
    # not used to run the application, of no use"""
    apk del .tmp-build-deps
    # adduser \
    #     --disabled-password \
    #     --no-create-home \
    #     django-user
# RUN chown -R django-user:django-user /app
ENV PATH="/py/bin:$PATH"

# USER django-user