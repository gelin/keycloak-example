FROM python:3-alpine

RUN apk add --no-cache \
    gcc musl-dev libffi-dev openssl-dev python3-dev

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=app.py

ENTRYPOINT [ "flask", "run" ]
