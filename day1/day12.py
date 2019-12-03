import os

def getData():
    inFile = open('data.txt', 'r')
    lines = inFile.readlines()
    inFile.close()
    return lines

def rocketScience(mass):
    return (mass // 3) - 2

def main():
    result = 0
    inData = getData()
    for i in inData:
        result += rocketScience(int(i))
    return result

print(main())