from os import error
import sys
import math

def parseNumber(string):
    # Needs recursion:
    # - push numbers into array
    # - when [ occurs, add new recursion layer
    # - when ] occurs, return recursed number so far
    # - when , occurs, skip

    number = []
    for i in range(len(string)):
        c = string[i]
        if c == ',':
            continue

        if c == '[':
            n1, remaining = parseNumber(string[i+1:])
            number.append(n1)
            n2, remaining = parseNumber(remaining)
            number.extend(n2)
            return number, remaining

        if c == ']':
            return number, string[i+1:]
        number.append(int(c))
    
    return number, ''

def readInput(inputfile):
    input = []
    with open(inputfile) as file:
        lineFound = True

        while lineFound:
            line = file.readline()
            if not line:
                lineFound = False
            else:
                line = line.strip()

                lineWoFirstArray = line[1: len(line)-1]
                number, remaining = parseNumber(lineWoFirstArray)
                input.append(number)
    return input

def reduce(number):
    depth = 0

    for i in range(len(number)):
        position = number[i]
        print(position)
        if isinstance(position, list):
            if depth >= 3:
                print("Need to explode {}".format(position))

def solutionPart1(input):
    for number in input:
        print(number)
        reduce(number)

def solutionPart2(input):
    print(input)

if __name__ == "__main__":
    part = int(sys.argv[1])
    inputfile = sys.argv[2]
    

    print("Solution {} for file {}".format(part, inputfile))

    input = readInput(inputfile)
    if part == 1:
        solutionPart1(input)

    else:
        solutionPart2(input)

