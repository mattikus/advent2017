#!/usr/bin/env python3

import sys

def find_bottom(tower):
    trunks = set()
    branches = set()

    for line in tower:
        try:
            prog, children = line.strip().split(" -> ")
        except ValueError:
            continue

        progname, weight = prog.split()
        trunks.add(progname)
        branches.update(children.split(', '))

    return (trunks - branches).pop()


if __name__ == "__main__":
    tower = sys.stdin.readlines()
    print(find_bottom(tower))
