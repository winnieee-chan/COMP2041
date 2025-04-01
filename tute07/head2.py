#!/usr/bin/python3
import sys

def head(lines, n):
    for i in range(0, n):
        print(lines[i].rstrip('\n'))

n = 5
files = []
for arg in sys.argv[1:]:
    if arg.startswith('-'):
        n = int(arg) * -1
    else:
        files.append(arg)

for file_name in files:
    with open(file_name, 'r') as file:
        lines = file.readlines()
        head(lines, n)
    print()
