from vars import *
import re
import spacy


def extract_holding(text: str, nlp: spacy.Language):
    doc = nlp(text)
    sents = list(doc.sents)
    holdings = []
    for i in range(len(sents)):
        sent = sents[i]
        start, end = sent.start, sent.end
        tokens = doc[start:end]
        for t in tokens:
            if t.lemma_ == 'hold' and (USE_LEMMA_ONLY or t.pos_ == 'VERB'):
                ii = max(i - 1, 0)
                jj = min(i + 1, len(sents) - 1)
                start, end = sents[ii].start, sents[jj].end
                text = doc[start:end].text
                text = re.sub(r'\n', ' ', text)
                holdings.append(text)
    return holdings
