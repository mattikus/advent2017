#!/usr/bin/env python3

import sys

def check(row):
    nums = [int(x) for x in row.split()]
    for idx, x in enumerate(nums):
        for y in nums[idx+1:]:
            if x % y == 0:
                return x // y
            if y % x == 0:
                return y // x

if __name__ == "__main__":
	sheet = sys.stdin.readlines()
    print(sum(check(row) for row in sheet))
