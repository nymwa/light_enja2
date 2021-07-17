import sys

if __name__ == '__main__':
    for line in sys.stdin:
        en, ja = line.strip().split('\t')
        en_len = len(en.split())
        ja_len = len(ja.split())
        if 4 <= en_len <= 16 and 4 <= ja_len <= 16:
            print(en + '\t' + ja)

