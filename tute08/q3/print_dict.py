#!/usr/bin/env python3

dict = {"key": "value", "andrew": "green", "anne": "red", "John": "blue"}

print(dict.items())

for k, val in dict.items():
    print(f"[{k}] => {val}")
