import sys

def load_enja():
    en_list = []
    ja_list = []
    for line in sys.stdin:
        en, ja = line.strip().split('\t')
        en_list.append(en)
        ja_list.append(ja)
    return en_list, ja_list

if __name__ == '__main__':
    en_list = []
    ja_list = []
    for line in sys.stdin:
        en, ja = line.strip().split('\t')
        en_list.append(en)
        ja_list.append(ja)

    en_dict = {sent: 0 for sent in en_list}
    ja_dict = {sent: 0 for sent in ja_list}

    for en, ja in zip(en_list, ja_list):
        if en_dict[en] == 0 and ja_dict[ja] == 0:
            en_dict[en] += 1
            ja_dict[ja] += 1
            print(en + '\t' + ja)

