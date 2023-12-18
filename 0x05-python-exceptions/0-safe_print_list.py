#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    number = 0
    while number < x:
        try:
            print("{}".format(my_list[length]), end="")
        except IndexError:
            print("index error occured")
            break
        number +=i 1
    print("")
    return number
