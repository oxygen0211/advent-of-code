import sys
import numpy as np
from numpy.lib.function_base import gradient

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
                input.append([int(n) for n in line])
    return input

numberByLength = {
    2: [1],
    3: [7],
    4: [4],
    5: [2, 3, 5],
    6: [0, 6, 9],
    7: [8]
}

def calculateMinima(input):
    minima = []
    for y in range(len(input)):
        for x in range(len(input[y])):
            num = input[y][x]
            minimum = True
            if x > 0:
                minimum = minimum and num < input[y][x-1]
            
            if x < len(input[y])-1:
                minimum = minimum and num < input[y][x+1]
            
            if y > 0:
                minimum = minimum and num < input[y-1][x]
            
            if y < len(input)-1:
                minimum = minimum and num < input[y+1][x]
            
            if minimum:
                minima.append({"x": x, "y": y, "height": num})

    return minima

def solutionPart1(input):
    riskLevels = []
    for minimum in calculateMinima(input):
        risk = 1 + minimum["height"]
        riskLevels.append(risk)
    
    print("Risk levels: {}".format(riskLevels))
    print("Answer: {}".format(sum(riskLevels)))

def checkIfBasin(val, ref):
    if val == 9:
        return False

    if val > ref:
        return True
    
    return False

def findBasin(input, x, y, ref):
    basin = []
    if x > 0:
        neighbor = input[y][x-1]
        if checkIfBasin(neighbor, ref):
            basin.append({"x": x-1, "y": y, "height": neighbor})
            basin.extend(findBasin(input, x-1, y, neighbor))
    
    if x < len(input[y]) - 1:
        neighbor = input[y][x+1]
        if checkIfBasin(neighbor, ref):
            basin.append({"x": x+1, "y": y, "height": neighbor})
            basin.extend(findBasin(input, x+1, y, neighbor))
    
    if y > 0:
        neighbor = input[y-1][x]
        if checkIfBasin(neighbor, ref):
            basin.append({"x": x, "y": y-1, "height": neighbor})
            basin.extend(findBasin(input, x, y-1, neighbor))

    if y < len(input) - 1:
        neighbor = input[y+1][x]
        if checkIfBasin(neighbor, ref):
            basin.append({"x": x, "y": y+1, "height": neighbor})
            basin.extend(findBasin(input, x, y+1, neighbor))

    return basin

def solutionPart2(input):
    print(input)
    minima = calculateMinima(input)

    basinSizes = []
    for minimum in minima:
        basin = [minimum]
        basin.extend(findBasin(input, minimum["x"], minimum["y"], minimum["height"]))

        filtered = []
        for point in basin:
            if point not in filtered:
                filtered.append(point)
        for point in filtered:
            print("x: {}, y:{}".format(point["x"], point["y"]))

        length = len(filtered)
        print("Basin size: {}".format(length))
        basinSizes.append(length)
    
    basinSizes.sort()
    print(basinSizes)
    top = basinSizes[-3:]
    answer = 1
    for l in top:
        answer *= l
    print("Largest 3: {} Answer: {}".format(top, answer))

if __name__ == "__main__":
    part = int(sys.argv[1])
    inputfile = sys.argv[2]

    print("Solution {} for file {}".format(part, inputfile))

    input = readInput(inputfile)
    if part == 1:
        solutionPart1(input)

    else:
        solutionPart2(input)

