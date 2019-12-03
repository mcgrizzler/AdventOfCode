datas = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,9,19,23,2,23,10,27,1,27,5,31,1,31,6,35,1,6,35,39,2,39,13,43,1,9,43,47,2,9,47,51,1,51,6,55,2,55,10,59,1,59,5,63,2,10,63,67,2,9,67,71,1,71,5,75,2,10,75,79,1,79,6,83,2,10,83,87,1,5,87,91,2,9,91,95,1,95,5,99,1,99,2,103,1,103,13,0,99,2,14,0,0]

def process(data):
    done = False
    pos = 0
    while not done:

        # If Opt-code = 1
        # Add
        if data[pos] == 1:
            pos1 = data[pos + 1]
            pos2 = data[pos + 2]
            loc = data[pos + 3]
            added = data[pos1] + data[pos2]
            data[loc] = added

            if pos == len(data) - 4:
                done = True
            else:
                done = False
                pos += 4

        # If Opt-code = 2
        # Multiply
        if data[pos] == 2:
            pos1 = data[pos + 1]
            pos2 = data[pos + 2]
            loc = data[pos + 3]
            multiplied = data[pos1] * data[pos2]
            data[loc] = multiplied


            if pos == len(data) - 4:
                done = True
            else:
                done = False
                pos += 4

        # If Opt-code = 99
        # Exit
        if data[pos] == 99:
            done = True

    return data


def main():
    inData = datas
    noun = 0
    verb = 0
    done = False
    while not done:
        inData[1] = noun
        inData[2] = verb
        output = process(inData)
        if output[0] == 19690720 and noun < 100:
            done = True
            print ('Noun: {}\nVerb: {}'.format(noun, verb))
        elif output[0] != 19690720 and noun < 100:
            noun += 1
            verb += 1
            inData = datas
            done = False
        else:
            done = False

        

main()