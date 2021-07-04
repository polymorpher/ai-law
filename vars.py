import os
from dotenv import load_dotenv

load_dotenv()

DATA_PATH = os.getenv('DATA_PATH', '/Volumes/s/CircuitCourtData/cases by year/2010_complete')
TEXT_OUT_PATH = os.getenv('TEXT_OUT_PATH', '/Volumes/s/CircuitCourtDataText/2010')
HOLDING_OUT_PATH = os.getenv('HOLDING_OUT_PATH', '/Volumes/s/CircuitCourtDataHoldings/2010')
USE_POS = (os.getenv('USE_POS') == 'true' or os.getenv('USE_POS') == '1')

if USE_POS:
    print('Using Lemma+POS')
else:
    print('Using lemma only')
