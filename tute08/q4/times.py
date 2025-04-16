#!/usr/bin/env python3
import sys


rows = int(sys.argv[1])
cols = int(sys.argv[2])
col_width = int(sys.argv[3])

for r in range(1, rows + 1):
    for c in range(1, cols + 1):
        print(str(r * c).rjust(col_width), end="")

    print()
