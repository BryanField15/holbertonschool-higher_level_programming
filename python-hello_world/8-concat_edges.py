#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
words = str.split()
middle_words = ' '.join(words[5:8])
first_word = words[0]
str = f"{middle_words} with {first_word}"
print(str)
