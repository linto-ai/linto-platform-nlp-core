# linto-platform-nlp-core

## Description
This repository is for building core Docker image for LinTO's NLP services, can be deployed along with [LinTO stack](https://github.com/linto-ai/linto-platform-stack) or in an standalone way (see Develop section in below).

linto-platform-nlp-core is backed by [spaCy](https://spacy.io/) v3.0+ featuring transformer-based pipelines, thus deploying with GPU support is highly recommeded for inference efficiency.

LinTo's NLP services adopt the basic design concept of spaCy: [component and pipeline](https://spacy.io/usage/processing-pipelines), componets are decoupled from the service and can be easily re-used in other projects, components are organised into pipelines for realising specific NLP tasks. 

This service uses [FastAPI](https://fastapi.tiangolo.com/) to serve spaCy's build-in components as pipelines:
- `ner`: Named Entity Recognition

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

2 Run container (with GPU), make sure that [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#installing-on-ubuntu-and-debian) and GPU driver are installed.
```bash
sudo docker run --gpus all --rm -d -p 80:80 lintoai/linto-platform-nlp-core:latest
```
<details>
  <summary>Check running with CPU only setting</summary>
  
  ```bash
  sudo docker run --rm -d -p 80:80 lintoai/linto-platform-nlp-core:latest
  ```
</details>

To lanche with multiple workers, add `--workers INTEGER` in the end of the above command.

3 Navigate to `http://localhost/docs` or `http://localhost/redoc` in your browser, to explore the REST API interactively. See the examples for how to query the API.


## Specification for `http://localhost/ner/{lang}`
### Supported languages
| {lang} | Model | `ner` Labels |
| --- | --- | --- |
| `en` | [xx_ent_wiki_sm-3.1.0](https://github.com/explosion/spacy-models/releases/tag/xx_ent_wiki_sm-3.1.0) | `LOC`, `MISC`, `ORG`, `PER` |
| `fr` | [xx_ent_wiki_sm-3.1.0](https://github.com/explosion/spacy-models/releases/tag/xx_ent_wiki_sm-3.1.0) | `LOC`, `MISC`, `ORG`, `PER` |

### Request
```json
{
  "articles": [
    {
      "text": "Apple Inc. is an American multinational technology company that specializes in consumer electronics, computer software and online services."
    },
    {
      "text": "Apple was founded in 1976 by Steve Jobs, Steve Wozniak and Ronald Wayne to develop and sell Wozniak's Apple I personal computer."
    }
  ]
}
```

### Response
```json
{
  "ner": [
    {
      "text": "Apple Inc. is an American multinational technology company that specializes in consumer electronics, computer software and online services.",
      "ents": [
        {
          "text": "Apple Inc",
          "label": "ORG",
          "start": 0,
          "end": 9
        },
        {
          "text": "American",
          "label": "MISC",
          "start": 17,
          "end": 25
        }
      ]
    },
    {
      "text": "Apple was founded in 1976 by Steve Jobs, Steve Wozniak and Ronald Wayne to develop and sell Wozniak's Apple I personal computer.",
      "ents": [
        {
          "text": "Apple",
          "label": "ORG",
          "start": 0,
          "end": 5
        },
        {
          "text": "Steve Jobs",
          "label": "PER",
          "start": 29,
          "end": 39
        },
        {
          "text": "Steve Wozniak",
          "label": "PER",
          "start": 41,
          "end": 54
        },
        {
          "text": "Ronald Wayne",
          "label": "PER",
          "start": 59,
          "end": 71
        },
        {
          "text": "Wozniak",
          "label": "PER",
          "start": 92,
          "end": 99
        },
        {
          "text": "Apple I",
          "label": "MISC",
          "start": 102,
          "end": 109
        }
      ]
    }
  ]
}
```

