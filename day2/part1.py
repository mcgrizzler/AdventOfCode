data = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,9,19,23,2,23,10,27,1,27,5,31,1,31,6,35,1,6,35,39,2,39,13,43,1,9,43,47,2,9,47,51,1,51,6,55,2,55,10,59,1,59,5,63,2,10,63,67,2,9,67,71,1,71,5,75,2,10,75,79,1,79,6,83,2,10,83,87,1,5,87,91,2,9,91,95,1,95,5,99,1,99,2,103,1,103,13,0,99,2,14,0,0
]


done = False

pos = 0
curOpCode = data[pos]


while not done:
    
    if curOpCode == 1:
        num1 = data[data[pos + 1]]
        print(num1)
        num2 = data[data[pos + 2]]
        print(num2)
        loc = data[pos + 3]
        print(loc)
        data[loc] = (num1 + num2)
        print(num1 + num2)
        pos += 4
        curOpCode = data[pos]
        if pos == len(data) - 4:
            done = True
        else:
            done = False

    if curOpCode == 2:
        num1 = data[data[pos + 1]]
        print(num1)
        num2 = data[data[pos + 2]]
        print(num2)
        loc = data[pos + 3]
        print(loc)
        data[loc] = (num1 * num2)
        pos += 4
        curOpCode = data[pos]
        if pos == len(data) - 4:
            done = True
        else:
            done = False

    if curOpCode == 99:
        done = True

print(data)


