#!/usr/bin/env python

from __future__ import print_function

def count_orbits(orbits, name):
    if name in orbits:
        return 1 + count_orbits(orbits, orbits[name])
    else:
        return 0

def main():
    with open('6-input.txt') as f:
        orbits = { pair[1]:pair[0] for pair in map(lambda x: x.split(")"), f) }
    print(sum(map(lambda x: count_orbits(orbits, x), orbits.keys())))

if __name__ == '__main__':
    main()
