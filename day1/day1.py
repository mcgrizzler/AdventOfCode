import os

def getData():
    inFile = ('data.txt', 'r')
    lines = inFile.readlines()
    inFile.close()
    return lines

print(getData())