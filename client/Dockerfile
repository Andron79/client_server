FROM python:latest

ADD client.py /client/

WORKDIR /client/
ADD requirements.txt ./
RUN pip install  --no-cache-dir -r requirements.txt