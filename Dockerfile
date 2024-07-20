FROM python:3.11-alpine3.20

COPY requirements.txt /temp/requirements.txt
COPY weather /weather
WORKDIR /weather
EXPOSE 27

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password app-user

USER app-user