FROM python:3.11-slim

WORKDIR /home/speckle

COPY requirements.txt /home/speckle/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /home/speckle


