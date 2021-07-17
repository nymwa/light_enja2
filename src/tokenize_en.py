import sys
import re
import unicodedata
from sacremoses import MosesTokenizer

def preproc_en(mt, x):
    x = unicodedata.normalize('NFKC', x)
    x = re.sub(mt.AGGRESSIVE_HYPHEN_SPLIT[0], r'\1 - ', x)
    x = mt.tokenize(x, escape = False)
    x = ' '.join(x)
    x = x.lower()
    return x

def main():
    mt = MosesTokenizer(lang = 'en')

    for line in sys.stdin:
        x = line.strip()
        x = preproc_en(mt, x)
        print(x)

if __name__ == '__main__':
    main()

