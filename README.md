# linto-platform-nlp-core

## Description
This repository is for building a core Docker image for LinTO's NLP services, can be deployed along with [LinTO stack](https://github.com/linto-ai/linto-platform-stack) or in an standalone way (see Develop section in below).

linto-platform-nlp-core is backed by [spaCy](https://spacy.io/) v3.0+ featuring transformer-based pipelines, thus deploying with GPU support is highly recommeded for inference efficiency.

LinTo's NLP services adopt the basic design concept of spaCy: [component and pipeline](https://spacy.io/usage/processing-pipelines), components are decoupled from the service and can be easily re-used in other projects, components are organised into pipelines for realising specific NLP tasks. 

This is a void service served by [FastAPI](https://fastapi.tiangolo.com/).

## Usage

See documentation : [https://doc.linto.ai](https://doc.linto.ai)

## Deploy

With our proposed stack [https://github.com/linto-ai/linto-platform-stack](https://github.com/linto-ai/linto-platform-stack)

# Develop

## Build and run
1 Build image
```bash
cd linto-platform-nlp-core/
sudo docker build --tag lintoai/linto-platform-nlp-core:latest .
```

2 Run container with GPU support, make sure that [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#installing-on-ubuntu-and-debian) and GPU driver are installed.
```bash
sudo docker run --gpus all \
--rm -p 80:80 \
lintoai/linto-platform-nlp-core:latest \
--workers 1
```
<details>
  <summary>Check running with CPU only setting</summary>
  
  - remove `--gpus all` from the above command.
</details>

3 Navigate to `http://localhost/docs` or `http://localhost/redoc` in your browser, to explore the REST API interactively. See the examples for how to query the API.
