import sys
from collections import defaultdict

def load_enja():
    en_list = []
    ja_list = []
    for line in sys.stdin:
        en, ja = line.strip().split('\t')
        en_list.append(en)
        ja_list.append(ja)
    return en_list, ja_list


def make_enja_dict(en_list, ja_list):

    en_dict = defaultdict(int)
    for sent in en_list:
        for word in sent.split():
            en_dict[word] += 1

    ja_dict = defaultdict(int)
    for sent in ja_list:
        for word in sent.split():
            ja_dict[word] += 1

    return en_dict, ja_dict


def make_enja_freq(en_dict, ja_dict):

    en_freq = list(en_dict.items())
    en_freq.sort(key = lambda x: -x[1])

    ja_freq = list(ja_dict.items())
    ja_freq.sort(key = lambda x: -x[1])

    return en_freq, ja_freq


def make_enja_filtered_set(en_freq, ja_freq):

    en_filtered_set = {word
            for word, freq
            in en_freq if freq >= 7}

    ja_filtered_set = {word
            for word, freq
            in ja_freq if freq >= 5}

    return en_filtered_set, ja_filtered_set


def check(filtered_set, text):
    return all(word in filtered_set for word in text.split())


if __name__ == '__main__':
    en_list, ja_list = load_enja()
    en_dict, ja_dict = make_enja_dict(en_list, ja_list)
    en_freq, ja_freq = make_enja_freq(en_dict, ja_dict)
    en_filtered_set, ja_filtered_set = make_enja_filtered_set(en_freq, ja_freq)

    for en, ja in zip(en_list, ja_list):
        if check(en_filtered_set, en) and check(ja_filtered_set, ja):
            print(en + '\t' + ja)

