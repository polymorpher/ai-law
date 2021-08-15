from vars import *
import os
from pathlib import Path
from nlp import nlp_init
import html_extractor
import holding_extractor


class Extractor:
    def __init__(self, data_path=CACHE, text_out_path=CACHE_OUT,
                 holiding_out_path=CACHE_HOLDING):
        self.nlp = nlp_init()
        self.data_path = data_path
        self.text_out_path = text_out_path
        self.holiding_out_path = holiding_out_path
        self.cleaner = html_extractor.build_cleaner()
        self.parser = html_extractor.build_parser()
        os.makedirs(data_path, exist_ok=True)
        os.makedirs(text_out_path, exist_ok=True)
        os.makedirs(holiding_out_path, exist_ok=True)

    def local_extract_text_all(self):
        files = os.listdir(Path(self.data_path))
        files = sorted(files)
        for fname in files:
            if fname.startswith('.'):
                continue
            if not fname.endswith('.html'):
                continue
            self.local_extract_text(fname)

    def local_extract_text(self, fname):
        p = os.path.join(self.data_path, fname)
        print(f'Reading {p}')
        html_content = Path(p).read_text()
        text, texts = html_extractor.extract_html(html_content, parser=self.parser, cleaner=self.cleaner)
        if not text:
            return
        o = os.path.join(self.text_out_path, fname.split('.')[0] + '.txt')
        Path(o).write_text(text)

    def local_extract_holdings_all(self):
        files = os.listdir(Path(self.text_out_path))
        files = sorted(files)
        combined = []
        for fname in files:
            if fname.startswith('.'):
                continue
            if not fname.endswith('.txt'):
                continue
            print(f'Processing {fname}')
            p = os.path.join(self.text_out_path, fname)
            text = Path(p).read_text()
            holdings = holding_extractor.extract_holding(text, self.nlp)

            if len(holdings) > 0:
                holding_all = ' '.join(holdings)
                o = os.path.join(self.holiding_out_path, fname)
                Path(o).write_text(holding_all)
                combined.extend(holdings)
        all_holdings_text = '\n'.join(combined)  # [f'{r}' for r in combined]
        Path(os.path.join(self.holiding_out_path, 'all.csv')).write_text(all_holdings_text)
        # input('Press any key to continue:')

    def list_all_text_files(self):
        return os.listdir(Path(self.text_out_path))

    def list_all_holding_files(self):
        return os.listdir(Path(self.holiding_out_path))
