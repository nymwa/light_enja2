import sys
import re
import unicodedata
from tqdm import tqdm
from sacremoses import MosesTokenizer
import spacy

def preproc_en(mt, x):
    x = unicodedata.normalize('NFKC', x)
    x = re.sub(mt.AGGRESSIVE_HYPHEN_SPLIT[0], r'\1 - ', x)
    x = mt.tokenize(x, escape = False)
    x = ' '.join(x)
    x = x.lower()
    return x

def preproc_ja(nlp, x):
    x = unicodedata.normalize('NFKC', x)
    x = nlp(x)
    x = [token.text for token in x]
    x = ' '.join(x)
    return x


if __name__ == '__main__':
    mt = MosesTokenizer(lang = 'en')
    nlp = spacy.load('ja_ginza')

    for line in tqdm(sys.stdin):
        x = line.strip().split('\t')
        en = preproc_en(mt, x[1])
        ja = preproc_ja(nlp, x[3])
        print(en + '\t' + ja)


