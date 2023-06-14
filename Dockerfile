FROM pytorch/pytorch:1.8.1-cuda10.2-cudnn7-runtime
LABEL maintainer="gshang@linagora.com"

RUN apt-get update &&\
    apt-get install -y gcc &&\
    apt-get clean

WORKDIR /usr/src/app

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
