import spacy

_nlp: spacy.Language = None


def nlp_init() -> spacy.Language:
    global _nlp
    if not _nlp:
        _nlp = spacy.load('en_core_web_sm', disable=['ner', 'textcat'])
        print('pipelines:', _nlp.pipe_names)
    return _nlp
