#!/usr/bin/python3
for p in range(122, 96, -1):
    if p % 2 != 0:
        p = p - 32
    print("{}".format(chr(p)), end='')
