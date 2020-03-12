FROM python:3.7-slim

ARG PROG_NAME
ENV PROG_NAME=$PROG_NAME

WORKDIR /usr/src/app
COPY ./app .
RUN [ -f requirements.txt ] &&\
    pip install --no-cache-dir -r requirements.txt

CMD python ${PROG_NAME}

