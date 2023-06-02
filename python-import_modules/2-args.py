#!/usr/bin/python3

import sys


def print_args():
    count = len(sys.argv) - 1
    if count == 0:
        print("{} arguments.".format(count))
    if count == 1:
        print("{} argument:".format(count))
        print("{}: {}".format(count, sys.argv[1]))
    if count > 1:
        print("{} arguments:".format(count))
        for i in range(1, count + 1):
            print("{}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    print_args()
