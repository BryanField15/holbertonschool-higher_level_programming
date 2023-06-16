#!/usr/bin/python3
"""
Module containing one function that changes indentation and spacing
"""


def text_indentation(text):
    """
    Function that that prints a text with 2 new lines after each of these
    characters: ., ? and :

    Args:
        text: string to be modified

    Return:
        Modified string printed to terminal
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in [".", "?", ":"]:
        text = text.replace(char, char.strip() + "\n\n")
    text = '\n'.join(line.strip() for line in text.split('\n'))
    print(text, end="")
