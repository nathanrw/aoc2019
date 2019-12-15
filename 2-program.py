#!/usr/bin/env python

from __future__ import print_function

OP_TERMINATE=99
OP_ADD=1
OP_MUL=2

def run(p):
    i = 0
    while True:
        if i < 0 or i >= len(p): 
            raise RuntimeError("Instruction pointer out of bounds.")
        op = p[i]
        if op == OP_TERMINATE:
            break # Done
        elif op == OP_ADD or op == OP_MUL:
            if len(p) - i <= 3:
                raise RuntimeError("Not enough arguments for binary operator.")
            ia = p[i+1]
            if ia < 0 or ia >= len(p):
                raise RuntimeError("Invalid input address 1.")
            a = p[ia]
            ib = p[i+2]
            if ib < 0 or ib >= len(p):
                raise RuntimeError("Invalid input address 2.")
            b = p[ib]
            j = p[i+3] # output address
            if j < 0 or j >= len(p):
                raise RuntimeError("Invalid output address.")
            if op == OP_ADD:
                p[j] = a + b
            elif op == OP_MUL:
                p[j] = a * b
            else:
                raise RuntimeError("Unknown binary operation.")
            i += 4
        else:
            raise RuntimeError("Unknown opcode.")

def main():
    with open('2-input.txt') as f:
        program_lines = map(lambda l: map(lambda i: int(i), l.split(',')), f)
        program = [ num for line in program_lines for num in line ]
        program[1] = 12
        program[2] = 2
        run(program)
        print(program[0])

if __name__ == '__main__':
    main()
