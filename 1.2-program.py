#!/usr/bin/env python

from __future__ import print_function

def fuel_cost(mass):
    cost = mass // 3 - 2
    if cost <= 0: return 0
    return cost + fuel_cost(cost)

def main():
    with open('1-input.txt') as masses:
        cost = sum(map(lambda mass: fuel_cost(int(mass)), masses))
        print(cost)

if __name__ == '__main__':
    main()
