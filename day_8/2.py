#!/usr/bin/env python

import sys
from collections import defaultdict

OP_TABLE = {
    '>': '__gt__',
    '<': '__lt__',
    '>=': '__ge__',
    '<=': '__le__',
    '==': '__eq__',
    '!=': '__ne__',
}

def process(instructions):
    registers = defaultdict(int)
    biggest = 0

    def passes_conditional(reg, op, value):
        return getattr(registers[reg], OP_TABLE[op])(int(value))


    for line in instructions:
        ops = line.split()
        register = ops[0]
        value = int(ops[2])
        if passes_conditional(*ops[4:]):
            if ops[1] == 'inc':
                registers[register] += value
            else:
                registers[register] -= value

        biggest = max(registers.values()) if max(registers.values()) > biggest else biggest

    return biggest



if __name__ == "__main__":
    instructions = sys.stdin.readlines()
    print(process(instructions))

