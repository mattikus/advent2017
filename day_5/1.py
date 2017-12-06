#!/usr/bin/env python3

import sys

def get_out(instructions):
    idx = 0
    steps = 0
    out = len(instructions)

    while idx < out:
        jump = instructions[idx]
        instructions[idx] += 1
        idx += jump
        steps += 1

    return steps

if __name__ == "__main__":
    instructions = [int(x) for x in sys.stdin.readlines()]
    print(get_out(instructions))
