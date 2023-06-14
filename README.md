# linto-platform-nlp-core

## Description
This repository is for building a core Docker image holding the common dependencies for all LinTO's NLP services:
- [named-entity-recognition](https://github.com/linto-ai/linto-platform-nlp-named-entity-recognition)
- [keyphrase-extraction](https://github.com/linto-ai/linto-platform-nlp-keyphrase-extraction)
- [extractive-summarization](https://github.com/linto-ai/linto-platform-nlp-extractive-summarization)
- [topic-modeling](https://github.com/linto-ai/linto-platform-nlp-topic-modeling)

## Usage
See documentation : [https://doc.linto.ai](https://doc.linto.ai)


## Build image
```bash
cd linto-platform-nlp-core/
sudo docker build --tag lintoai/linto-platform-nlp-core:latest .
```
or
```bash
sudo docker-compose build
```
