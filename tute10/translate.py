#!/usr/bin/env python3

"""
Syntax:
str.maketrans(x, y, z)

Parameters:
- x and y: Two strings of equal length, mapping characters in x to characters in y.
- z: A string of characters to remove.
"""


# Replace 'a' with '1', 'b' with '2', and remove 'c'
table = str.maketrans("ab", "12", "c")
print("abc cab".translate(table))
# Output: '12 12'
