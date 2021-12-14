FROM pytorch/pytorch:1.8.1-cuda10.2-cudnn7-runtime
LABEL maintainer="gshang@linagora.com"

RUN apt-get update &&\
    apt-get install -y gcc &&\
    apt-get clean

WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY ./scripts /app/scripts
COPY ./components /app/components

HEALTHCHECK --interval=15s CMD curl -fs http://0.0.0.0/health || exit 1

ENTRYPOINT ["/opt/conda/bin/gunicorn", "scripts.main:app", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:80", "--access-logfile", "-", "--error-logfile", "-"]
CMD ["--workers", "1"]