import sys

def load_enja():
    en_list = []
    ja_list = []
    for line in sys.stdin:
        en, ja = line.strip().split('\t')
        en_list.append(en)
        ja_list.append(ja)
    return en_list, ja_list


right = 1.8
left = 0.5
def check(en, ja):
    en_len = len(en.split())
    ja_len = len(ja.split())
    return left <= (en_len / ja_len) <= right


if __name__ == '__main__':
    en_list, ja_list = load_enja()

    for en, ja in zip(en_list, ja_list):
        if check(en, ja):
            print(en + '\t' + ja)

