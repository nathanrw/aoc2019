#!/usr/bin/env python

from __future__ import print_function

def validate(number, range_min, range_max):
    if number < range_min or number > range_max: return False
    current = 0
    adjacent = False
    for digit in str(number):
        value = int(digit)
        if value < current:
            return False
        if value == current:
            adjacent = True
        current = value
    return adjacent

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
