#!/usr/bin/env python

from __future__ import print_function

class Move(object):
    def __init__(self, code):
        self.dir = code[0]
        self.distance = int(code[1:])

class Point(object):
    def __init__(self, x, y, steps):
        self.pos = (x, y)
        self.steps = steps
    def __hash__(self): return self.pos.__hash__()
    def __eq__(self, that): return self.pos.__eq__(that.pos)

def trace(wire):
    steps = 0
    points = [Point(0, 0, steps)]
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
        x, y = points[-1].pos
        for i in range(move.distance):
            steps += 1
            x += dx
            y += dy
            points.append(Point(x, y, steps))
    return points

def manhattan(point):
    return abs(point.pos[0]) + abs(point.pos[1])

def main():
    with open('3-input.txt', 'r') as f:
        wires = list(map(lambda line: map(Move, line.split(",")), f))
        trace0 = trace(wires[0])
        trace1 = trace(wires[1])
        # Note: wont work, need both steps.
        intersections = set(trace0) & set(trace1)
        sorted_intersections = sorted(intersections, key=lambda x: x.steps)
        closest = sorted_intersections[1] # avoid 0, 0
        print("Closest: %s, %s" % closest.pos)
        print("Distance: %s" % manhattan(closest))

if __name__ == '__main__':
    main()
