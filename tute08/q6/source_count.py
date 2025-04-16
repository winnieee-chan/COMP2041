#!/usr/bin/env python3

import glob

print(glob.glob("*.[ch]"))

total = 0
for filename in glob.glob("*.[ch]"):
    with open(filename, "r") as f:
        n = len(f.readlines())
        total += n

        print(f"{str(n).rjust(8)} {filename}")


print(f"{str(total).rjust(8)} total")
