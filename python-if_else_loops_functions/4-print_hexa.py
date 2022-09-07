#!/usr/bin/python3
string = "{:d} = 0x{:x}"
for i in range(99):
    print(string.format(i, i))
