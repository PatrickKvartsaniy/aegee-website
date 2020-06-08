FROM python:3.7-alpine

WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc musl-dev jpeg-dev zlib-dev

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app/

ENV SQL_DATABASE=aegee
ENV SQL_USER=patrick
ENV SQL_PASSWORD=erasmusmundus
ENV SQL_HOST=127.0.0.1
ENV SQL_PORT=5432

EXPOSE 8080

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]