import spacy
import components

from typing import Dict, List

from celery_app.celeryapp import celery

from extractive-summarization.extsumm import logger
from extsumm.processing import LM_MAP, MODELS, get_model
from extsumm.processing.utils import get_data

from kpe import logger
from kpe.processing import LM_MAP, MODELS, get_model
from kpe.processing.utils import get_data

from ner import logger
from ner.processing import LM_MAP, MODELS
from ner.processing.utils import get_data

from topic import logger
from topic.processing import LM_MAP, MODELS, get_model
from topic.processing.utils import get_data

@celery.task(name="extsumm_task")
def extsumm_task(lang: str, texts: List[str], component_cfg: Dict = {}):
    """Process a batch of articles and return the extractive summary predicted by the
    given model. Each record in the data should have a key "text".
    """
    logger.info('ExtSumm task received')

    # Check language availability
    if lang in LM_MAP.keys():
        model_name = LM_MAP[lang]
        if model_name not in MODELS.keys():
            raise RuntimeError(f"Model {model_name} for language {lang} is not loaded.")
        nlp = spacy.blank(lang)
        nlp.add_pipe("sentencizer", config={"punct_chars": ['|']})
        nlp.add_pipe("extsumm", config={"model": {"@misc": "get_model", "name": model_name}})
    else:
        raise ValueError(f"Language {lang} is not supported.")

    response_body = []
    
    for doc in nlp.pipe(texts, component_cfg=component_cfg):
        response_body.append(get_data(doc))

    return {"extsumm": response_body}


@celery.task(name="kpe_task")
def kpe_task(lang: str, texts: List[str], component_cfg: Dict = {}):
    """Process a batch of articles and return the Keyphrases predicted by the
    given model. Each record in the data should have a key "text".
    """
    logger.info('KPE task received')

    # Check language availability
    if lang in LM_MAP.keys():
        model_name = LM_MAP[lang]
        if model_name not in MODELS.keys():
            raise RuntimeError(f"Model {model_name} for language {lang} is not loaded.")
        nlp = spacy.blank(lang)
        nlp.add_pipe("kpe", config={"model": {"@misc": "get_model", "name": model_name}})
    else:
        raise ValueError(f"Language {lang} is not supported.")
    
    response_body = []

    for doc in nlp.pipe(texts, component_cfg=component_cfg):
        response_body.append(get_data(doc))

    return {"kpe": response_body}

@celery.task(name="ner_task")
def ner_task(lang: str, texts: List[str], component_cfg: Dict = {}):
    """ ner_task """
    logger.info('NER task received')

    # Check language availability
    if lang in LM_MAP.keys():
        model_name = LM_MAP[lang]
        if model_name not in MODELS.keys():
            raise RuntimeError(f"Model {model_name} for language {lang} is not loaded.")
        nlp = MODELS[model_name]
    else:
        raise ValueError(f"Language {lang} is not supported.")

    response_body = []
    
    for doc in nlp.pipe(texts, component_cfg=component_cfg):
        response_body.append(get_data(doc))

    return {"ner": response_body}

@celery.task(name="topic_task")
def topic_task(lang: str, texts: List[str], component_cfg: Dict = {}):
    """Process a batch of articles and return the extractive summary predicted by the
    given model. Each record in the data should have a key "text".
    """
    logger.info('Topic task received')

    # Check language availability
    if lang in LM_MAP.keys():
        model_name = LM_MAP[lang]
        if model_name not in MODELS.keys():
            raise RuntimeError(f"Model {model_name} for language {lang} is not loaded.")
        nlp = spacy.blank(lang)
        nlp.add_pipe("sentencizer", config={"punct_chars": ['|']})
        nlp.add_pipe("topic", config={"model": {"@misc": "get_model", "name": model_name}})
    else:
        raise ValueError(f"Language {lang} is not supported.")

    response_body = []
    
    for doc in nlp.pipe(texts, component_cfg=component_cfg):
        response_body.append(get_data(doc))

    return {"topic": response_body}


