#!/usr/bin/env python3

from glob import glob

total_lines = 0
for file_name in glob("*.[ch]"):
    with open(file_name, "r") as file:
        num_lines = len(file.readlines())
        total_lines += num_lines
        print(f"{str(num_lines).rjust(8)} {file_name}")

print(f"{str(total_lines).rjust(8)} total")