import os

def processData():
    inFile = open('data3.txt', 'r')
    lines = inFile.readlines()
    inFile.close()
    return lines

print(processData())