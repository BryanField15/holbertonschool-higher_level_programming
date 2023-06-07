#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        missing_elements = 2 - len(tuple_a)
        zeros_tuple = (0,) * missing_elements
        tuple_a += zeros_tuple
    if len(tuple_b) < 2:
        missing_elements = 2 - len(tuple_b)
        zeros_tuple = (0,) * missing_elements
        tuple_b += zeros_tuple
    tuple_to_list = []
    for i in range(2):
        tuple_to_list.append(tuple_a[i] + tuple_b[i])
        new_tuple = tuple(tuple_to_list)
    return new_tuple
