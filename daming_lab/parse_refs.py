import pandas as pd
import numpy as np
import pandas
import re
import os
# from graphviz import Graph

from bs4 import BeautifulSoup

judges = []
edges = []

stopwords = ['Before', 'Chief', 'Judge', 'and', 'Circuit', 'Judges']

f_out = open("summaries.html", "w")
# f_out = open("summaries.txt", "w")


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
    global f_out
    soup = BeautifulSoup(file_loc, 'html.parser')
    opinion_texts = soup.findAll("p", class_="opinion_text")
    sentences = []
    for opinion_text in opinion_texts:
        pure_text_raw = opinion_text.text
        pure_text_raw = pure_text_raw.replace('\n', '')
        pure_text = pure_text_raw.replace('\t', '')
        if len(pure_text) < 150:
            continue
        if not any(c.islower() for c in pure_text):
            continue

        print('check')
        if 'hold' in pure_text_raw or 'held' in pure_text_raw:
            sentences.append(opinion_text)
            f_out.write(str(opinion_text) + '<br />')
            f_out.flush()
    print('done')
    print(sentences)


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
    cnt = 1
    for file_loc in files:
        fp = open(file_loc)
        file_name = os.path.basename(file_loc)
        parse_one_html_file(file_name, fp)
        cnt -= 1
        # if cnt <= 0:
        #     break

    # draw DAG graph
    # print('final done')
    # import ipdb;ipdb.set_trace()
    # print('haha')
    # dot = Graph()
    # for j in judges:
    #     dot.node(j, j)
    # for e in edges:
    #     dot.edge(e[0], e[1])
    # print('finally')
    # file_name = 'finally'
    # dot.render(file_name, view=True)

    print('end')
