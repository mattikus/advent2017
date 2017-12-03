#!/usr/bin/env python3

import sys

def check(row):
    nums = [int(x) for x in row.split()]
    low = high = nums[0]
    for num in nums[1:]:
        if num < low:
            low = num
            continue
        if num > high:
            high = num

    return high - low

if __name__ == "__main__":
	sheet = sys.stdin.readlines()
    print(sum(check(row) for row in sheet))
