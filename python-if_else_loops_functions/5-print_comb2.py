#!/usr/bin/python3
for numbers in range(0, 100):
    if (numbers < 10):
        print("0{}, ".format(numbers), end="")
    elif (numbers == 99):
        print("{}".format(numbers))
    else:
        print("{}, ".format(numbers), end="")
