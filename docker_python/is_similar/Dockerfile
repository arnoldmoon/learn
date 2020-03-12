ARG BASE=python
ARG TAG=3.7-slim

FROM ${BASE}:${TAG}

ARG PROG_NAME=__main__.py
ENV PROG_NAME=$PROG_NAME

WORKDIR /usr/src/app
COPY ./app .
RUN [ -f requirements.txt ] &&\
    pip install --no-cache-dir -r requirements.txt

CMD python ${PROG_NAME}

