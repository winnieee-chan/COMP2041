#!/usr/bin/env python3
import sys

n_rows = int(sys.argv[1])
n_cols = int(sys.argv[2])
col_width = int(sys.argv[3])

for r in range(1, n_rows + 1):
    for c in range(1, n_cols + 1):
        print(f"{str(r*c).rjust(col_width)}", end="")
    
    print()