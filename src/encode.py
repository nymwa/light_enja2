import sys
import sentencepiece as spm
from argparse import ArgumentParser

def sp_encode(sp, f, alpha=None):
    for x in f:
        x = x.strip()
        x = ' '.join(x.split())
        if alpha is None:
            x = sp.encode(x, out_type = int)
        else:
            x = sp.encode(x, out_type = int, enable_sampling = True, alpha = alpha)
        x = ' '.join([sp.IdToPiece(i) for i in x])
        print(x)

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-m', '--model')
    parser.add_argument('-a', '--alpha', type=float, default=None)
    args = parser.parse_args()

    sp = spm.SentencePieceProcessor()
    sp.Load(args.model)
    sp_encode(sp, sys.stdin, alpha=args.alpha)

