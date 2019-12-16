#!/usr/bin/env python

from __future__ import print_function

class Move(object):
    def __init__(self, code):
        self.dir = code[0]
        self.distance = int(code[1:])

def trace(wire):
    points = [(0, 0)]
    for move in wire:
        dy, dx = 0, 0
        if move.dir == "U":
            dy = 1
        elif move.dir == "D":
            dy = -1
        elif move.dir == "R":
            dx = 1
        elif move.dir == "L":
            dx = -1
        else:
            raise RuntimeError("Unknown direction.")
        x, y = points[-1]
        for i in range(move.distance):
            x += dx
            y += dy
            points.append((x, y))
    return points

def manhattan(point):
    return abs(point[0]) + abs(point[1])

def main():
    with open('3-input.txt', 'r') as f:
        wires = list(map(lambda line: map(Move, line.split(",")), f))
        trace0 = trace(wires[0])
        trace1 = trace(wires[1])
        intersections = set(trace0) & set(trace1)
        sorted_intersections = sorted(intersections, key=manhattan)
        closest = sorted_intersections[1] # avoid 0, 0
        print("Closest: %s, %s" % closest)
        print("Distance: %s" % manhattan(closest))

if __name__ == '__main__':
    main()
