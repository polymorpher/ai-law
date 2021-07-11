import pandas as pd
import numpy as np
import pandas
import re
import os
from graphviz import Graph

from bs4 import BeautifulSoup

judges = []
edges = []

stopwords = ['Before', 'Chief', 'Judge', 'and', 'Circuit', 'Judges']

def parse_one_html_file_old(file_name, file_loc):
    soup = BeautifulSoup(file_loc, 'html.parser')
    print('soup')
    # print(soup)
    sentences = []
    opinion_texts = soup.findAll("p", class_="opinion_text")
    print('opinion_texts')
    # print(opinion_texts)
    for opinion_text in opinion_texts:
        pure_text_raw = opinion_text.text
        pure_text_raw = pure_text_raw.replace('\n', '')
        pure_text = pure_text_raw.replace('\t', '')
        if len(pure_text) < 150:
            continue
        if not any(c.islower() for c in pure_text):
            continue
        sentences.append(pure_text)

    print('sentences for {}'.format(file_name))
    print(sentences)


def parse_one_html_file(file_name, file_loc):
    soup = BeautifulSoup(file_loc, 'html.parser')
    paras = soup.findAll("div")
    cur_judges = []
    # if file_name == 'x1q6lfa5ji82.html':
    #     print('x1q6lfa5ji82.html')
    # if 'x1q6lee6kfo2' in file_name:
    #     print('x1q6lee6kfo2')
    #     import ipdb;ipdb.set_trace()
    # if 'x1dc73m003' in file_name:
    #     print('x1dc73m003')
    #     import ipdb;ipdb.set_trace()

    if 'x1cvgd0003.html' in file_name:
        print('debug')
        import ipdb;ipdb.set_trace()

    for para in paras:
        pure_text_raw = para.text
        pure_text_raw = pure_text_raw.strip()
        if 'Before' in pure_text_raw:
            # print('in')
            pure_text_raw = pure_text_raw.strip()

        if pure_text_raw.startswith('Before'):
            print(pure_text_raw)
            pure_text_raw = pure_text_raw[len('Before'):]
            # if pure_text_raw[0] == ':':
            #     pure_text_raw = pure_text_raw[1:]
            # front_back = pure_text_raw.split('and')
            # front = front_back[0]
            # back = front_back[1]
            # index = front.find(',')
            # one = front[:index]
            # two = front[:index+1]
            # index = back.find(',')
            # three = back[:index]
            # print('|'.join([one, two, three]))
            # words = re.findall(r'[^,;:\s]+', front)
            # for word in words:
            #     if word not in stopwords:
            #

            words = re.findall(r'[^,;:\s]+', pure_text_raw)
            cur_judge_name = []
            for word in words:
                word = word.strip()
                if word.isupper() and len(word) > 3:
                    cur_judges.append(word)
                    if word not in judges:
                        judges.append(word)
            #     else:
            #         if len(cur_judge_name) > 0:
            #             cur_judge_name_full = ' '.join(cur_judge_name)
            #             if cur_judge_name_full not in judges:
            #                 judges.append(cur_judge_name_full)
            #             cur_judges.append(cur_judge_name_full)
            #             cur_judge_name = []
            # if len(cur_judge_name) > 0:
            #     cur_judge_name_full = ' '.join(cur_judge_name)
            #     if cur_judge_name_full not in judges:
            #         judges.append(cur_judge_name_full)
            #     cur_judges.append(cur_judge_name_full)
            break
    cur_judges = sorted(cur_judges)
    print('{} has judges {}'.format(file_name, cur_judges))
    for i in range(0, len(cur_judges)):
        for j in range(i+1, len(cur_judges)):
            cur_edge = [cur_judges[i], cur_judges[j]]
            if cur_edge not in edges:
                edges.append(cur_edge)
    print('hmmmm')
    print('done')


if __name__ == '__main__':
    import ipdb;ipdb.set_trace()
    # files = ['./2010_complete/x1e5ggk003.html', './2010_complete/x1e6b54003.html']
    folder = './2010_complete'
    current_dir = os.path.dirname(os.path.abspath(__file__))
    target_folder = os.path.join(current_dir, folder)
    files = []
    for f in os.listdir(target_folder):
        if not f.endswith('html'):
            continue
        # print(f)
        # print('done')
        files.append(os.path.join(
            target_folder,
            f
        ))
    print('next')
    cnt = 100
    for file_loc in files:
        fp = open(file_loc)
        file_name = os.path.basename(file_loc)
        parse_one_html_file(file_name, fp)
        cnt -= 1
        if cnt <= 0:
            break

    print('final done')
    import ipdb;ipdb.set_trace()
    print('haha')
    dot = Graph()
    for j in judges:
        dot.node(j, j)
    for e in edges:
        dot.edge(e[0], e[1])
    print('finally')
    file_name = 'finally'
    dot.render(file_name, view=True)

    print('end')
