#!/usr/bin/env python3

import sys

# from collections import Counter
import collections

weights = sys.argv[1:]


freq = collections.Counter(weights)

max_weight = float("-inf")
max_num = None
for k, v in freq.items():
    curr_weight = int(k) * v
    if curr_weight > max_weight:
        max_weight = curr_weight
        max_num = k


print(max_num)
