#!/usr/bin/env python3

import subprocess
import sys
import re
import collections
import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument(
    "-f", "--frequency", help="Order by frequency", action="store_true"
)
argparser.add_argument("url", help="url to fetch")

args = argparser.parse_args()

# Get the html
process = subprocess.run(
    ["wget", "-q", "-O-", args.url], capture_output=True, text=True
)
html = process.stdout.lower()

# Remove comments
html = re.sub("<!--.*", "", html)

# Find all the tags
tags = re.findall(r"<\s*(\w+)", html)
counter = collections.Counter(tags)

items = counter.items()

if args.frequency:
    items = sorted(items, key=lambda x: x[1])

for tag, count in items:
    print(f"{tag}: {count}")
