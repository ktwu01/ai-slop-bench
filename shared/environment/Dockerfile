FROM python:3.12-slim

# UTF-8 everywhere: the tasks and the delivered answers are Chinese text.
ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    PYTHONIOENCODING=utf-8 \
    PYTHONDONTWRITEBYTECODE=1

# curl/bash/node are what Harbor's agent installers look for. pytest is baked in
# at build time so the verifier needs no network.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        bash ca-certificates curl git nodejs npm procps \
    && apt-get clean

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app
