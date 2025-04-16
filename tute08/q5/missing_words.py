#!/usr/bin/env python3
import sys

file1_name = sys.argv[1]
file2_name = sys.argv[2]


def get_words_in_file(file_name):
    list_of_words = set()
    with open(file_name, "r") as file:
        lines = file.readlines()
        for line in lines:
            words = line.split(" ")
            for word in words:
                list_of_words.add(word.strip())
    return list_of_words


file1_words = get_words_in_file(file1_name)
file2_words = get_words_in_file(file2_name)

missing_words = []
for word in file1_words:
    if word not in file2_words:
        missing_words.append(word)

missing_words.sort()
print(" ".join(missing_words))
