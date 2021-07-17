import sys
import random as rd

def write_corpus(name, lst):
    with open('{}.en'.format(name), 'w') as f, open('{}.ja'.format(name), 'w') as g:
        for en, ja in lst:
            print(en, file = f)
            print(ja, file = g)

if __name__ == '__main__':
    lst = []
    for line in sys.stdin:
        en, ja = line.strip().split('\t')
        lst.append((en, ja))

    rd.shuffle(lst)
    train = lst[:-10000]
    valid = lst[-10000:-5000]
    test = lst[-5000:]

    write_corpus('train', train[:int(len(train) / 10000) * 10000])
    write_corpus('valid', valid)
    write_corpus('test', test)


