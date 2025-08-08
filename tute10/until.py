#!/usr/bin/env python3

import sys
import re


# int
# /regex/

address = sys.argv[1]
is_regex = False

if address.startswith("/"):
    is_regex = True
    address = address[1:-1]
else:
    address = int(address)

counter = 1
while True:
    try:
        line = input()
        print(line)

        if is_regex:
            if re.search(address, line):
                break
        else:
            if counter == address:
                break
        counter += 1
    except:
        break
