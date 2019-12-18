#!/usr/bin/env python

from __future__ import print_function

import argparse

OP_TERMINATE=99
OP_ADD=1
OP_MUL=2
OP_READ=3
OP_WRITE=4
OP_JUMP_IF_TRUE=5
OP_JUMP_IF_FALSE=6
OP_LESS_THAN=7
OP_EQUALS=8

MODE_POSITION = 0
MODE_IMMEDIATE = 1

debug = False

def diagnostic(*args):
    if debug:
        print(">", *args)

def load_parameter(p, i, mode):
    if i < 0 or i >= len(p): raise RuntimeError("Invalid address.")
    val = p[i]
    if mode == MODE_POSITION:
        if val < 0 or val >= len(p): raise RuntimeError("Invalid address.")
        return p[val]
    elif mode == MODE_IMMEDIATE:
        return val
    else:
        raise RuntimeError("Unknown parameter mode.")

def decode_op(opmode):
    mode1 = (opmode // 100) % 10
    mode2 = (opmode // 1000) % 10
    mode3 = (opmode // 10000) % 10
    op = opmode % 100
    ret = (op, mode1, mode2, mode3)
    diagnostic(opmode, "->", *ret)
    return ret

def run(p, inputs=[]):
    p = [integer for integer in p] # copy
    i = 0
    outputs = []
    while True:
        if i < 0 or i >= len(p): 
            raise RuntimeError("Instruction pointer out of bounds.")
        op, mode1, mode2, mode3 = decode_op(p[i])
        if op == OP_TERMINATE:
            break # Done
        elif op == OP_ADD or \
             op == OP_MUL or \
             op == OP_LESS_THAN or \
             op == OP_EQUALS:
            if len(p) - i <= 3:
                raise RuntimeError("Not enough arguments for binary operator.")
            a = load_parameter(p, i+1, mode1)
            b = load_parameter(p, i+2, mode2)
            j = load_parameter(p, i+3, MODE_IMMEDIATE)
            if j < 0 or j >= len(p):
                raise RuntimeError("Invalid output address.")
            if op == OP_ADD:
                p[j] = a + b
            elif op == OP_MUL:
                p[j] = a * b
            elif op == OP_LESS_THAN:
                p[j] = int(a < b)
            elif op == OP_EQUALS:
                p[j] = int(a == b)
            else:
                raise RuntimeError("Unknown binary operation.")
            i += 4
        elif op == OP_READ:
            if len(p) - i <= 1:
                raise RuntimeError("Not enough arguments for read.")
            j = load_parameter(p, i+1, MODE_IMMEDIATE)
            if len(inputs) == 0:
                p[j] = 0
            else:
                p[j] = inputs.pop(0)
            i += 2
        elif op == OP_WRITE:
            if len(p) - i <= 1:
                raise RuntimeError("Not enough arguments for write.")
            a = load_parameter(p, i+1, mode1)
            outputs.append(a)
            print(a)
            i += 2
        elif op == OP_JUMP_IF_TRUE or op == OP_JUMP_IF_FALSE:
            if len(p) - i <= 2:
                raise RuntimeError("Not enough arguments for jump.")
            a = load_parameter(p, i+1, mode1)
            j = load_parameter(p, i+2, mode2)
            jump = (op == OP_JUMP_IF_TRUE and a) or \
                    (op == OP_JUMP_IF_FALSE and not a)
            if jump:
                # Note: only validate jump address if we're actually going to
                # jump, since the address might be bad if the condition is
                # false.
                if j < 0 or j >= len(p):
                    raise RuntimeError("Invalid jump address.")
                i = j
            else:
                i += 3
        else:
            raise RuntimeError("Unknown opcode.")
    return outputs

def main():
    parser = argparse.ArgumentParser(description="Day 5 part 2.")
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()
    global debug
    debug = args.debug
    with open('5-input.txt') as f:
        program_lines = map(lambda l: map(lambda i: int(i), l.split(',')), f)
        program = [ num for line in program_lines for num in line ]
        run(program, [5])

if __name__ == '__main__':
    main()
