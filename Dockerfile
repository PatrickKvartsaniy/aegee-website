FROM python:3.7-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc musl-dev jpeg-dev zlib-dev

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /usr/src/app/

EXPOSE 8080

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]