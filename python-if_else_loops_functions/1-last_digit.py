#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

if number >= 0:
    last_digit = number % 10
else:
    last_digit = -1 * ((-1 * number) % 10)

str1 = 'Last digit of'
str2 = 'and is less than 6 and not 0'
str3 = 'and is greater than 5'

if (last_digit > 5):
    print("{} {} is {} {}".format(str1, number, last_digit, str3))

elif (last_digit == 0):
    print("{} {} is {} and is 0".format(str1, number, last_digit))

else:
    print("{} {} is {} {}".format(str1, number, last_digit, str2))
