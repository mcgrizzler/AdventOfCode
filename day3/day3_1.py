from aoc import read_file, timer

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

def main():
    inData = read_file('data3.txt')
    wire1 = inData[0].split(',')
    wire2 = inData[1].split(',')

    pos1 = drawWire(wire1)
    pos2 = drawWire(wire2)

    intersects = pos1.intersection(pos2)

    return min([distance(pos) for pos in intersects])

print('Solution: {}'.format(main()))