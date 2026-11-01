# Dockerfile:jeff
#
# Base build environment
#

FROM python:3.14-slim-trixie
LABEL maintainer="Jeffrey Carpenter <jeff@479831.xyz>"

ARG VERSION=1.0.0

USER root
WORKDIR /
RUN apt-get update && apt-get install -y python3-venv git bash net-tools

#
RUN mkdir -p /app
COPY requirements.txt /app
USER app
WORKDIR /app

# expose inside container
ENV \
  PYTHONUTF8=1 \
  LC_ALL=C.UTF-8 \
  VERSION=${VERSION}

RUN python3 -m venv /app/venv &&
  /app/venv/bin/pip3 install discord.py requests &&
  python3 -m build
#RUN python3 -m pip install /app/dist/update_ddns_zone-${VERSION}-py3-none-any.whl

