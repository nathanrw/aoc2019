#!/usr/bin/env python

from __future__ import print_function

def main():
    with open('1-input.txt') as masses:
        fuel_cost = sum(map(lambda mass: int(mass) // 3 - 2, masses))
        print(fuel_cost)

if __name__ == '__main__':
    main()
