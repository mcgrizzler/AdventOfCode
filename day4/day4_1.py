# Advent of Code 2019
# Day 4 Part 1

def main(data):
    result = []
    for c in data:
        c = list(str(c))
        isSequence = processSequence(c)
        hasDoubles = processDoubles(c)

        if isSequence and hasDoubles:
            result.append(c)

    return len(result)

def pullData():
    # List of all codes between:
    # 123257 and 647015
    return list(range(123257, 647016))

def processSequence(data):
    count = 1
    isSequence = True

    for _ in data:
        _ = int(_)
        if _ <= int(data[count]) and count < 5:
            isSequence = True
            count += 1
        elif _ <= int(data[count]) and count == 5:
            isSequence = True
            break
        else:
            isSequence = False
            break
    
    return isSequence

def processDoubles(data):
    count = 1
    hasDouble = False
    for _ in data:
        _ = int(_)

        if count == 6:
            break

        if _ == int(data[count]) and count < 6:
            hasDouble = True
            break
        elif _ != int(data[count]) and count < 6:
            count += 1
        elif _ != int(data[count]) and count == 6:
            break

        

    return hasDouble


inData = pullData()
#inData = [112345]
print(main(inData))