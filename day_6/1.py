#!/usr/bin/env python3

import sys

def realloc(blocks):
    count = pos = 0
    banks = len(blocks)
    for idx, num in enumerate(blocks):
        if num > count:
            count = num
            pos = idx

    blocks[pos] = 0
    while count > 0:
        pos += 1
        blocks[pos % banks] += 1
        count -= 1

    return blocks

def collapse(blocks):
    return "".join(str(x) for x in blocks)

def balance(blocks):
    seen = [collapse(blocks)]

    blocks = realloc(blocks)
    while collapse(blocks) not in seen:
        seen.append(collapse(blocks))
        blocks = realloc(blocks)

    return len(seen)

if __name__ == "__main__":
    blocks = [int(x) for x in sys.stdin.readline().strip().split()]
    print(balance(blocks))
