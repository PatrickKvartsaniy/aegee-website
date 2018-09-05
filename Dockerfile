FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /website

WORKDIR /website

ADD . /website/

RUN pip install -r requirements.txt