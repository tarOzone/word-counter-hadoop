#!./venv python3

import re
import sys


def read_input(file):
    for line in file:
        line = line.lower()
        line = re.sub("[^a-zA-Z0-9\n]", " ", line)
        yield line.split()


def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    for words in data:
        for word in words:
            out = f"{word}{separator}{1}" + "\n"
            sys.stdout.write(out)


if __name__ == "__main__":
    main()
