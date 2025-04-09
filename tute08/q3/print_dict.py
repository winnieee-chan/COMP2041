#!/usr/bin/env python3
def print_dict():
    d = {
        "key":"value",
        "andrew": "green",
        "anne": "red",
        "John": "blue"
    }

    for key in d:
        print(f"[{key}] => {d[key]}")

print_dict()