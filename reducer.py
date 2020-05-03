#!./venv python3

import sys
from itertools import groupby
from operator import itemgetter


def read_mapper_output(separator='\t'):
    for line in sys.stdin:
        yield line.rstrip().split(separator, 1)


def main(separator='\t'):
    data = read_mapper_output(separator=separator)
    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for curr_word, count in group)
            out = f"{current_word}{separator}{total_count}" + "\n"
            sys.stdout.write(out)
        except ValueError as e:
            pass


if __name__ == "__main__":
    main()
