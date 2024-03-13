FROM python:3.9-slim

RUN apt-get update && apt-get install -y --no-install-recommends gcc wget libpq-dev build-essential libcrypt1

WORKDIR /braille

RUN pip install --upgrade pip
ADD requirements.txt /braille/requirements.txt
RUN pip install -r /braille/requirements.txt

ENV PORT=8000
EXPOSE 8000