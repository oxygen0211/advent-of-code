from os import error
import sys
import math

def readInput(inputfile):
    input = []
    with open(inputfile) as file:
        lineFound = True

        while lineFound:
            line = file.readline()
            if not line:
                lineFound = False
            else:
                row = line.strip()
                input.append([int(n) for n in row])
    return input

def load(input):
    for y in range(len(input)):
            for x in range(len(input[y])):
                input[y][x] += 1
    return input

def flash(input, flashes):
    flashCoords = []
    for y in range(len(input)):
            for x in range(len(input[y])):
                if {'x': x, 'y': y} in flashes:
                    continue
                if input[y][x] > 9:
                    f = {'x': x, 'y': y}
                    flashCoords.append(f)
                    flashes.append(f)
    
    for flashCoord in flashCoords:
        x = flashCoord['x']
        y = flashCoord['y']

        if x > 0:
            input[y][x-1] += 1
            if y > 0:
                input[y-1][x-1] += 1
            
            if y < len(input) - 1:
                input[y+1][x-1] += 1
        
        if x < len(input[y]) - 1:
            input[y][x+1] += 1
            if y > 0:
                input[y-1][x+1] += 1
            if y < len(input) - 1:
                input[y+1][x+1] += 1

        if y > 0:
            input[y-1][x] += 1
        if y < len(input) - 1:
            input[y+1][x] += 1
    
    if len(flashCoords) > 0:
        flashes, input = flash(input, flashes)

    print("Flashes: {}".format(flashes))
    return flashes, input

def reset(input, flashes):
    for flash in flashes:
        x = flash['x']
        y = flash['y']
        input[y][x] = 0

    return input

def solutionPart1(input, steps):
    print(input)
    numFlashes = 0
    for step in range(steps):
        input = load(input)
        flashes, input = flash(input, [])
        input = reset(input, flashes)
        
        print("-----Step {}-----".format(step))
        for row in input:
            print(row)
        
        numFlashes += len(flashes)
    
    print("{} flashes after {} steps".format(numFlashes, steps))

def solutionPart2(input):
    print(input)
    numFlashes = 0
    boardHeight = len(input)
    boardWidth = len(input[0])
    entries = boardHeight * boardWidth
    
    simultaneousFlashes = 0
    steps = 0
    while simultaneousFlashes < entries:
        input = load(input)
        flashes, input = flash(input, [])
        simultaneousFlashes = len(flashes)
        input = reset(input, flashes)

        print("-----Step {}-----".format(steps))
        for row in input:
            print(row)
        
        steps += 1

    print("Fist time all flashed simultaneously was after {} steps".format(steps))

if __name__ == "__main__":
    part = int(sys.argv[1])
    inputfile = sys.argv[2]
    

    print("Solution {} for file {}".format(part, inputfile))

    input = readInput(inputfile)
    if part == 1:
        steps = int(sys.argv[3])
        solutionPart1(input, steps)

    else:
        solutionPart2(input)

