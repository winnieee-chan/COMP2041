#!/usr/bin/env python3
import sys


def main():
    for line in sys.stdin:
        words = line.split()
        words = reversed(words)
        print(" ".join(words))


if __name__ == "__main__":
    main()
