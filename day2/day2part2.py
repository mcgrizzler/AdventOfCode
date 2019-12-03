def readFile(file):
    with open(file, 'r') as f:
        data = list(map(int, f.read().split(',')))
    return data

def partOne(noun, verb):
    data = readFile('data.txt')
    data[1] = noun
    data[2] = verb
    pos = 0
    for i in data[::4]:
        if i == 1:
            addition = data[data[pos + 1]] + data[data[pos + 2]]
            location = data[pos + 3]
            data[location] = addition
        elif i == 2:
            multiplication = data[data[pos + 1]] * data[data[pos + 2]]
            location = data[pos + 3]
            data[location] = multiplication
        elif i == 99:
            break
        pos += 4
    return data[0]

def partTwo(output):
    for x in range(100):
        for y in range(100):
            if partOne(x, y) == output:
                return 100 * x + y

print(partOne(12, 2))
print(partTwo(19690720))
