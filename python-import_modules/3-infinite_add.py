#!/usr/bin/python3

import sys


def sum_args():
    total = 0

    for arg in sys.argv[1:]:
        int_arg = int(arg)
        total = total + int_arg
    print(total)


if __name__ == "__main__":
    sum_args()
