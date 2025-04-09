#!/usr/bin/python3
import sys

n = 10

if len(sys.argv) == 2:
    n = abs(int(sys.argv[1]))

# print(n)
lines = []
for line in sys.stdin:
    lines.append(line)


print(lines[:n])
for line in lines[:n]:
    print(line, end="")
