#!/usr/bin/env python3

import re
import collections
import argparse
import requests
from bs4 import BeautifulSoup

argparser = argparse.ArgumentParser()
argparser.add_argument(
    "-f", "--frequency", help="Order by frequency", action="store_true"
)
argparser.add_argument("url", help="url to fetch")

args = argparser.parse_args()

# Get the html
req = requests.get(args.url)
html = req.text

# # Remove comments
html = re.sub("<!--.*", "", html)

soup = BeautifulSoup(html, "html5lib")
tags = soup.find_all()

tag_names = [t.name for t in tags]
# Find all the tags
counter = collections.Counter(tag_names)

items = counter.items()

if args.frequency:
    items = sorted(items, key=lambda x: x[1])

for tag, count in items:
    print(f"{tag}: {count}")
