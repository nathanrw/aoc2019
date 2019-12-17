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

def find_intersections(trace1, trace2):
    steps1 = { point.pos: point.steps for point in trace1 }
    steps2 = { point.pos: point.steps for point in trace2 }
    points = set(steps1.keys()) & set(steps2.keys())
    intersections = \
            [Point(pos[0], pos[1], steps1[pos] + steps2[pos]) for pos in points]
    return sorted(intersections, key=lambda x: x.steps)

def manhattan(point):
    return abs(point.pos[0]) + abs(point.pos[1])

def main():
    with open('3-input.txt', 'r') as f:
        wires = list(map(lambda line: map(Move, line.split(",")), f))
        trace0 = trace(wires[0])
        trace1 = trace(wires[1])
        intersections = find_intersections(trace0, trace1)
        closest = intersections[1] # avoid 0, 0
        print("Closest: %s, %s" % closest.pos)
        print("Steps: %s" % closest.steps)
        print("Distance: %s" % manhattan(closest))

if __name__ == '__main__':
    main()
