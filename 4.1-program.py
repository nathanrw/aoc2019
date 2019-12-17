#!/usr/bin/env python

from __future__ import print_function

def validate(number, range_min, range_max):
    if number < range_min or number > range_max: return False
    current = 0
    runlength = 1
    adjacent = False
    for digit in str(number):
        value = int(digit)
        if value < current:
            return False
        elif value == current:
            runlength += 1
        else:
            adjacent = adjacent or runlength == 2
            runlength = 1
        current = value
    return adjacent or runlength == 2

def main():
    range_min = 382345
    range_max = 843167
    count = 0
    for x in range(range_min, range_max+1):
        if validate(x, range_min, range_max):
            count += 1
    print(count)

if __name__ == '__main__':
    main()
