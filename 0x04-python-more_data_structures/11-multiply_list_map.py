#!/usr/bin/python3
#function that returns a list with all values

def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))
