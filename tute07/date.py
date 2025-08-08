#!/usr/bin/env python3
import re

# Define the pattern with groups
pattern = r"(\d{4})-(\d{2})-(\d{2})"

# Compile the pattern
# You can compile a pattern so that you don't need to
# specify it every time when using search, match, fullmatch etc
regex = re.compile(pattern)

# Search for the pattern in a string
str = "Today is 2024-07-08, 2025-01-01."
non_match_str = "Today is a date"

match = regex.search(non_match_str)
# match1 = re.search(r"(\d{4})-(\d{2})-(\d{2})", str)
# match = regex.search(str)
# print("match1:", match1)
print("match:", match)

# Check if a match was found and access the groups
if match:
    # print(match.span())
    # start, end = match.span()
    # print(start)
    # print(end)
    # print(str[start:end])

    print("Entire match:", match.group(0))  # 2024-07-08
    print("Entire match:", match.group())  # 2024-07-08

    print("Year:", match.group(1))
    print("Month:", match.group(2))
    print("Day:", match.group(3))
else:
    print("No match found.")
