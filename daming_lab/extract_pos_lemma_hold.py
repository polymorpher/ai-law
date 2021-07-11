import spacy
import os
from bs4 import BeautifulSoup

nlp = spacy.load("en_core_web_sm")


def parse_one_html_file(file_name, file_loc, f_out):
    soup = BeautifulSoup(file_loc, 'html.parser')
    opinion_texts = soup.findAll("p", class_="opinion_text")
    sentences = []
    if 'x1dc73m003' in file_name:
        print('holdings')

    for i in range(0, len(opinion_texts)):
        opinion_text = opinion_texts[i]
        pure_text_raw = opinion_text.text
        pure_text_raw = pure_text_raw.replace('\n', '')
        pure_text = pure_text_raw.replace('\t', '')
        if len(pure_text) < 150:
            continue
        if not any(c.islower() for c in pure_text):
            continue
        # print('good sentence')
        text = (opinion_text.text)
        doc = nlp(text)
        # verbs = [token.lemma_ for token in doc if token.pos_ == "VERB"]
        # all tokens
        verbs = [token.lemma_ for token in doc]
        if 'hold' in verbs:
            f_out.write(str(opinion_text) + '<br />')
            f_out.flush()


if __name__ == '__main__':
    import ipdb;ipdb.set_trace()
    # files = ['./2010_complete/x1e5ggk003.html', './2010_complete/x1e6b54003.html']
    folder = '../2010_complete'
    current_dir = os.path.dirname(os.path.abspath(__file__))
    target_folder = os.path.join(current_dir, folder)
    files = []
    for f in os.listdir(target_folder):
        if not f.endswith('html'):
            continue
        files.append(os.path.join(
            target_folder,
            f
        ))

    # print(files)
    print(len(files))

    cnt = 1
    for file_loc in files:
        fp = open(file_loc)
        file_name = os.path.basename(file_loc)
        pieces = file_name.split('.')
        out_file = './out/' + pieces[0] + '_hold_not_only_verb.' + pieces[1]
        f_out = open(out_file, "w")
        parse_one_html_file(file_name, fp, f_out)
        cnt -= 1
        # if cnt <= 0:
        #     break
