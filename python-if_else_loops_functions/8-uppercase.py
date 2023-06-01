#!/usr/bin/python3

def uppercase(str):
    converted = ''
    for letters in str:
        if 97 <= ord(letters) <= 122:
            converted = converted + chr(ord(letters) - 32)
        else:
            converted = converted + letters

    print("{}".format(converted))
