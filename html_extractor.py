from vars import *
from lxml import html
from lxml.html.clean import Cleaner
import re


def build_parser():
    return html.HTMLParser(encoding='ascii')


def build_cleaner():
    cleaner = Cleaner()
    cleaner.javascript = True
    cleaner.style = True
    return cleaner


def extract_html(data: str, parser: html.HTMLParser, cleaner: Cleaner):
    tree = html.fromstring(data, parser=parser).getroot()
    selected = tree.cssselect('.opinion_text')
    texts = []
    if len(selected) < 1:
        print(f'File has no opinion text. Skipping')
        return None
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
    return text, texts
