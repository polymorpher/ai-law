from vars import *
from extractor import Extractor
from feeder import AWSFeeder
import re

if __name__ == '__main__':
    feeder = AWSFeeder()
    keys, dirs = feeder.list(prefix=S3_PATH)
    case_folder_re = r'.*/([0-9]+)_complete'
    print('keys', keys)
    print('dirs', dirs)
    case_dirs = [d for d in dirs if re.match(case_folder_re, d)]
    case_years = []
    for dir in case_dirs:
        m = re.match(case_folder_re, dir)
        case_years.append(m.group(1))
    year_keys, _ = feeder.list(prefix=case_dirs[0])

    print(case_dirs)
    print(year_keys)
    extractor = Extractor()


    def on_next(filename):
        frag = filename.split('/')[-1]
        extractor.local_extract_text(frag)


    def on_error(ex: Exception):
        print(ex)


    def key_processor(key):
        if not key.endswith('.html'):
            return None
        return key.split('/')[-1]


    # feeder.scan_prefix(prefix=case_dirs[0], key_processor=key_processor, on_next=on_next,
    #                    on_error=on_error)

    # extractor.local_extract_holdings_all()

    def upload_all(year):
        files = extractor.list_all_text_files()
        for f in files:
            k = S3_TEXT_OUT_PATH + concat(year, f)
            feeder.upload(key=k, filename=concat(extractor.text_out_path, f))
        print(f'[{year}] Uploaded {len(files)} extracted text files')
        files = extractor.list_all_holding_files()
        for f in files:
            k = S3_HOLDING_OUT_PATH + concat(year, f)
            feeder.upload(key=k, filename=concat(extractor.holiding_out_path, f))
        print(f'[{year}] Uploaded {len(files)} extracted holdings')


    upload_all(case_years[0])
