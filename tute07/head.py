#!/usr/bin/python3
import sys

n = 5

if len(sys.argv) == 2: 
    n = int(sys.argv[1]) * -1

lines = []
for line in sys.stdin: # Reads from stdin
    lines.append(line.strip('\n'))

# Option 1
# for i in range(0, n):
#     print(lines[i])

# Option 2
print("\n".join(lines[0:n]))

