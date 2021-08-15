from vars import *
import os
from pathlib import Path
from nlp import nlp_init
import html_extractor
import holding_extractor


class Extractor:
    def __init__(self, data_path=CACHE, out_path=CACHE_OUT, text_out_path=CACHE_OUT,
                 holiding_out_path=HOLDING_OUT_PATH):
        self.nlp = nlp_init()
        self.data_path = data_path
        self.out_path = out_path
        self.text_out_path = text_out_path
        self.holiding_out_path = holiding_out_path
        os.makedirs(data_path, exist_ok=True)
        os.makedirs(out_path, exist_ok=True)
        os.makedirs(text_out_path, exist_ok=True)
        os.makedirs(holiding_out_path, exist_ok=True)

    def local_extract_text(self):
        cleaner = html_extractor.build_cleaner()
        parser = html_extractor.build_parser()
        files = os.listdir(Path(self.data_path))
        files = sorted(files)
        for fname in files:
            if fname.startswith('.'):
                continue
            if not fname.endswith('.html'):
                continue
            p = os.path.join(self.data_path, fname)
            print(f'Reading {p}')
            html_content = Path(p).read_text()
            text, texts = html_extractor.extract_html(html_content, parser=parser, cleaner=cleaner)
            o = os.path.join(self.out_path, fname.split('.')[0] + '.txt')
            Path(o).write_text(text)

    def local_extract_holdings(self, ):
        files = os.listdir(Path(self.text_out_path))
        files = sorted(files)
        combined = []
        for fname in files:
            if fname.startswith('.'):
                continue
            if not fname.endswith('.txt'):
                continue
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
