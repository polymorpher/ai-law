from vars import *
from lxml import html
import os
from pathlib import Path
from lxml.html.clean import Cleaner
import re
import spacy


def extract_text():
    cleaner = Cleaner()
    cleaner.javascript = True
    cleaner.style = True
    files = os.listdir(Path(DATA_PATH))
    files = sorted(files)
    parser = html.HTMLParser(encoding='ascii')
    for fname in files:
        if fname.startswith('.'):
            continue
        if not fname.endswith('.html'):
            continue
        p = os.path.join(DATA_PATH, fname)
        print(f'Reading {p}')
        tree = html.parse(p, parser=parser).getroot()
        selected = tree.cssselect('.opinion_text')
        texts = []
        if len(selected) < 1:
            print(f'Skipped {p}')
            continue
        for el in selected:
            cleaned_tree = cleaner.clean_html(el)
            text = cleaned_tree.text_content().__str__()
            text = re.sub(r'[\n]?\[\*[0-9]+\][\n]?', '', text)
            # text = re.sub(r'\n+([a-zA-Z0-9,. ]+)', ' \g<1>', text)
            text = re.sub(r'[^\x09-\x7f]', '', text)
            text = re.sub(r'\n', ' ', text)
            text = re.sub(r'[ \t]+', ' ', text)
            texts.append(text)

        text = '\n'.join(texts)
        # print(text)
        # input('Press any key to continue:')
        o = os.path.join(TEXT_OUT_PATH, fname.split('.')[0] + '.txt')
        Path(o).write_text(text)


def extract_holdings():
    files = os.listdir(Path(TEXT_OUT_PATH))
    files = sorted(files)
    nlp = spacy.load('en_core_web_sm', disable=['ner', 'textcat'])
    print(nlp.pipe_names)
    combined = []
    for fname in files:
        if fname.startswith('.'):
            continue
        if not fname.endswith('.txt'):
            continue
        p = os.path.join(TEXT_OUT_PATH, fname)
        text = Path(p).read_text()
        doc = nlp(text)

        sents = list(doc.sents)
        holdings = []
        for i in range(len(sents)):
            sent = sents[i]
            start, end = sent.start, sent.end
            tokens = doc[start:end]
            for t in tokens:
                if t.lemma_ == 'hold' and ((not USE_POS) or t.pos_ == 'VERB'):
                    ii = max(i - 1, 0)
                    jj = min(i + 1, len(sents) - 1)
                    start, end = sents[ii].start, sents[jj].end
                    text = doc[start:end].text
                    text = re.sub(r'\n', ' ', text)
                    holdings.append(text)
        if len(holdings) > 0:
            holding_all = ' '.join(holdings)
            o = os.path.join(HOLDING_OUT_PATH, fname)
            Path(o).write_text(holding_all)
            combined.extend(holdings)
    all = '\n'.join(combined)  # [f'{r}' for r in combined]
    Path(os.path.join(HOLDING_OUT_PATH, 'all.csv')).write_text(all)
    # input('Press any key to continue:')


if __name__ == '__main__':
    os.makedirs(TEXT_OUT_PATH, exist_ok=True)
    os.makedirs(HOLDING_OUT_PATH, exist_ok=True)
    # extract_text()
    extract_holdings()
