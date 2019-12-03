from aoc import read_file, timer
from collections import defaultdict

def distance(pos):
    return abs(pos[0] + abs(pos[1]))

def drawWire(wire):
    x = 0
    y = 0
    positions = set()

    for i in range(len(wire)):
        for _ in range(int(wire[i][1:])):
            
            direction = wire[i][0]

            if direction == 'R':
                x += 1
            elif direction == 'L':
                x -= 1
            elif direction == 'D':
                y += 1
            elif direction == 'U':
                y -= 1

            positions.add((x, y))
    
    return positions

def getDistances(wire, intersects):
    intersectLoc = defaultdict(int)
    distance = 0
    x = 0
    y = 0

    for i in range(len(wire)):
        for _ in range(int(wire[i][1:])):

            direction = wire[i][0]

            if direction == 'R':
                x += 1
            elif direction == 'L':
                x -= 1
            elif direction == 'D':
                y += 1
            elif direction == 'U':
                y -= 1

            distance += 1

            if (x, y) in intersects:
                intersectLoc[(x, y)] = distance

    return intersectLoc

def main():
    inData = read_file('data3.txt')
    wire1 = inData[0].split(',')
    wire2 = inData[1].split(',')

    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0

    pos1 = drawWire(wire1)
    pos2 = drawWire(wire2)

    intersects = pos1.intersection(pos2)

    intersectDistance1 = getDistances(wire1, intersects)
    intersectDistance2 = getDistances(wire2, intersects)

    return min(intersectDistance1[intersect] + intersectDistance2[intersect] for intersect in intersects)

print('Solution: {}'.format(main()))