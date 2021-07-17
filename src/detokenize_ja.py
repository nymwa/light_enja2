import sys

def main():
    for line in sys.stdin:
        x = line.strip()
        x = ''.join(x.split())
        print(x)

if __name__ == '__main__':
    main()

