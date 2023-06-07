#!/usr/bin/python3
def multiple_returns(sentence):
    first = sentence[0]
    if sentence is None:
        first = None
        length = len(sentence)
        return length, first
