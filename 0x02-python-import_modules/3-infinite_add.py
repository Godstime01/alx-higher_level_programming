#!/usr/bin/python3

import sys

if __name__ == "__main__":
    ar = sys.argv
    total = 0
    for i in range(1, len(ar)):
        total += int(ar[i])
    print(total)
