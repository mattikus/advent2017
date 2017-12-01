#!/usr/bin/env python3

import sys

def inverse_captcha(captcha):
    arr = list(map(int, captcha))
    return sum(i for idx, i in enumerate(arr) if i == arr[(idx + (len(arr) // 2)) % len(arr)])

if __name__ == "__main__":
    problem_input = sys.argv[1]
    print(inverse_captcha(problem_input))
