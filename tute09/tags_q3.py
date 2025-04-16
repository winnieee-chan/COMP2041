#!/usr/bin/env python3

import subprocess
import sys
import re
import collections

url = sys.argv[1]
# Get the html
process = subprocess.run(["wget", "-q", "-O-", url], capture_output=True, text=True)
html = process.stdout.lower()

# Remove comments
html = re.sub("<!--.*", "", html)

# Find all the tags
tags = re.findall(r"<\s*(\w+)", html)
counter = collections.Counter(tags)

for tag, count in counter.items():
    print(f"{tag}: {count}")
