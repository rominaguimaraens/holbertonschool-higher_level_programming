#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list = len(my_list)
    for i in reversed(range(list)):
        print("{:d}".format(my_list[i]))
