#!/usr/bin/python3

import hidden_4

def print_names():
    names = dir(hidden_4)
    for target_name in names:
        if target_name[:2] != "__":
            print(target_name)

if __name__ == "__main__":
   print_names()
