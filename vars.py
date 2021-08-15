import os
from dotenv import load_dotenv

load_dotenv()

DATA_PATH = os.getenv('DATA_PATH', '/Volumes/s/CircuitCourtData/cases by year/2010_complete')
TEXT_OUT_PATH = os.getenv('TEXT_OUT_PATH', '/Volumes/s/CircuitCourtDataText/2010')
HOLDING_OUT_PATH = os.getenv('HOLDING_OUT_PATH', '/Volumes/s/CircuitCourtDataHoldings/2010')
USE_LEMMA_ONLY = (os.getenv('USE_LEMMA_ONLY') == 'true' or os.getenv('USE_LEMMA_ONLY') == '1')

if USE_LEMMA_ONLY:
    print('Using lemma only')
else:
    print('Using Lemma+POS')

S3_BUCKET = os.getenv('S3_BUCKET', 'ai-law')
S3_PATH = os.getenv('S3_PATH', 'cases/')
S3_TEXT_OUT_PATH = os.getenv('S3_TEXT_OUT_PATH', 'cases_processed/text/')
S3_HOLDING_OUT_PATH = os.getenv('S3_TEXT_OUT_PATH', 'cases_processed/holding/')

CACHE = os.getenv('CACHE', 'tmp/cache')
CACHE_OUT = os.getenv('CACHE_OUT', 'tmp/out')
CACHE_HOLDING = os.getenv('CACHE_HOLDING', 'tmp/holding')


def concat(*args, delim='/') -> str:
    return delim.join([a for a in args if a])
