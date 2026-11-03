# Dockerfile:jeff
#
# Base build environment
#

FROM python:3.14-slim-trixie
LABEL maintainer="Jeffrey Carpenter <jeff@479831.xyz>"

ARG VERSION=1.0.0

USER root
WORKDIR /
RUN set -eux \
    && DEBIAN_FRONTEND=noninteractive apt-get update -qq \
    && DEBIAN_FRONTEND=noninteractive apt-get install -qq -y --no-install-recommends --no-install-suggests \
    python3-venv \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && true

RUN mkdir -p /app
# TODO(JEFF): There is no reason why we cannot run this bot as a non-
# privileged user.
#USER app
WORKDIR /app
COPY .env /app
COPY .env.dist /app
COPY discord_bot.py /app
COPY LICENSE.md /app
COPY README.md /app
COPY requirements.txt /app
COPY TODO.md /app

# expose inside container
ENV \
  PYTHONUTF8=1 \
  LC_ALL=C.UTF-8 \
  VERSION=${VERSION}

RUN python3 -m venv /app/venv && \
  /app/venv/bin/pip3 install -r requirements.txt

ENTRYPOINT ["/app/venv/bin/python3", "/app/discord_bot.py"]
