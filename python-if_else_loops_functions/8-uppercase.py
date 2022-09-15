#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if i > 96 and i < 123:
            i = chr(ord(i) - 32)
        print("{:s}".format(i), end='')
    print(end='\n')
