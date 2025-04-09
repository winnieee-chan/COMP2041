#!/usr/bin/python3
import sys


def head(lines, n):
    for line in lines[:n]:
        print(line, end="")


n = 10
files = []
# read from arg
for arg in sys.argv[1:]:
    # check if we have optional -n
    if arg.startswith("-"):
        n = abs(int(arg))
    else:
        files.append(arg)


print("n: ", n)
print(files)

# read file names
for filename in files:
    print(f"first {n} lines in {filename}")
    # read from the file
    with open(filename, "r") as file:
        lines = file.readlines()
        head(lines, n)

    print()
