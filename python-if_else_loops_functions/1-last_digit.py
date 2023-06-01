#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
str1 = 'Last digit of'
str2 = 'and is less than 6 and not 0'
str3 = 'and is greater than 5'

if (0 < last_digit < 6):
    print("{} {:d} is {:d} {}".format(str1, number, last_digit, str2))

elif (last_digit > 5):
    print("{} {:d} is {:d} {}".format(str1, number, last_digit, str3))

else:
    print("{} {:d} is {:d} and is 0".format(str1, number, last_digit))
