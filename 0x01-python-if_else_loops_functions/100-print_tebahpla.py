#!/usr/bin/python3
lower = 32
for i in range(122, 96, -1):
    if lower == 0:
        lower = 32
    else:
        lower = 0
    print("{}".format(chr(i - lower)), end='')
