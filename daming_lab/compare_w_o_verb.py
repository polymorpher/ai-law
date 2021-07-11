import spacy
import os
from bs4 import BeautifulSoup
import shutil

if __name__ == '__main__':
    # files = ['./2010_complete/x1e5ggk003.html', './2010_complete/x1e6b54003.html']
    import ipdb;ipdb.set_trace()
    verb_and_lemma = './hold'
    only_lemma = './hold_not_only_verb'
    current_dir = os.path.dirname(os.path.abspath(__file__))
    out_folder = os.path.join(current_dir, './to_compare')
    verb_and_lemma_len = len(os.listdir(verb_and_lemma))
    print(verb_and_lemma_len)

    verb_and_lemma_files = []

    for verb_and_lemma_filename in os.listdir(verb_and_lemma):

        filename = verb_and_lemma_filename.split('.')[0].split('_')[0]
        # print(filename)
        verb_and_lemma_files.append(filename)
    

    only_lemma_files = []
    for verb_and_lemma_filename in os.listdir(only_lemma):

        filename = verb_and_lemma_filename.split('.')[0].split('_')[0]
        # print(filename)
        only_lemma_files.append(filename)    

    
    file_size_same = 0
    file_size_diff = 0

    for v in verb_and_lemma_files:
        if v in only_lemma_files:
            # print(only_lemma_files)
            vlf = v + '_hold_not_only_verb.html'
            vlf_loc = os.path.join(only_lemma, vlf)
            file_size1 = os.path.getsize(vlf_loc)
            shutil.copy(vlf_loc, os.path.join(out_folder, vlf))
            vlf = v + '_hold.html'
            vlf_loc = os.path.join(verb_and_lemma, vlf)
            file_size2 = os.path.getsize(vlf_loc)
            if file_size1 == file_size2:
                file_size_same += 1
            else:
                file_size_diff += 1
                print(vlf_loc)
            shutil.copy(vlf_loc, os.path.join(out_folder, vlf))
    
    print(file_size_same)
    print(file_size_diff)
