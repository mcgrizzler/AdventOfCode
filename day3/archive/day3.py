import os


#Open files and read them
with open('line1.txt', 'r') as f:
        line1 = list(map(str, f.read().split(',')))
        f.close()

with open('line2.txt', 'r') as f:
        line2 = list(map(str, f.read().split(',')))
        f.close()

# For Loops
line1coords = []
line2coords = []
x = 0
y = 0



for i in line1:

    command = i[:1]

    if command == 'D':
        # -y
        newY = y - int(i[1:])
        for ny in range(newY, y):
            line1coords.append((x, ny))
        y = newY
    if command ==  'U':
        # +y
        newY = y + int(i[1:])
        for ny in range(y, newY):
            line1coords.append((x, ny))
        y = newY
    if command == 'R':
        # +x
        newX = x + int(i[1:])
        for nx in range(x, newX):
            line1coords.append((nx, y))
        x = newX
    if command == 'L':
        # -x
        newX = x - int(i[1:])
        for nx in range(newX, x):
            line1coords.append((nx, y))
        x = newX

for i in line2:

    command = i[:1]

    if command == 'D':
        # -y
        newY = y - int(i[1:])
        for ny in range(newY, y):
            line2coords.append((x, ny))
        y = newY
    if command ==  'U':
        # +y
        newY = y + int(i[1:])
        for ny in range(y, newY):
            line2coords.append((x, ny))
        y = newY
    if command == 'R':
        # +x
        newX = x + int(i[1:])
        for nx in range(x, newX):
            line2coords.append((nx, y))
        x = newX
    if command == 'L':
        # -x
        newX = x - int(i[1:])
        for nx in range(newX, x):
            line2coords.append((nx, y))
        x = newX

result = []
pos = 0

for x in line2coords:
    print(x)
    if x[0] == line1coords[pos][0]:
        result.append(x)
    pos += 1



print(result)

print()