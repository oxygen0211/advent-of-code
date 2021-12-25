from os import error
import sys
from collections import Counter

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
                input.append([int(i) for i in line])
    return input

def findLeastRiskPathFrom(field, x, y):
    path = []
    point = field[y][x]
    
    xMax = len(field[0]) - 1
    yMax = len(field) - 1

    neighbors = []
    
    if x < len(field[0]) - 1:
        neighbors.append({"x": x+1, "y":y, "risk": field[y][x+1]})
    
    if y < len(field[0]) - 1:
        neighbors.append({"x": x, "y":y+1, "risk": field[y+1][x]})

    print("Neighbors: {}".format(neighbors))

    lowestRisk = 1000
    nextX = 0
    nextY = 0

    endReached = False
    minNeighborRisk = -1
    for neighbor in neighbors:
        if neighbor["x"] == xMax and neighbor["y"] == yMax:
            endReached = True
            lowestRisk = field[yMax][xMax]
            nextX = xMax
            nextY = yMax
            break

        if minNeighborRisk < 0 or neighbor["risk"] < minNeighborRisk:
            minNeighborRisk = neighbor["risk"]

    if not endReached:
        print("lowest risk for next step: {}".format(minNeighborRisk))
        for neighbor in neighbors:
            if neighbor["risk"] > minNeighborRisk:
                continue
            risk = findLeastRiskPathFrom(field, neighbor["x"], neighbor["y"])
            if risk < lowestRisk:
                lowestRisk = risk
                nextX = neighbor["x"]
                nextY = neighbor["y"]
    risk = point + lowestRisk
    print("Next step at {}, {} with risk {}.".format(nextX, nextY, risk))
    return risk

def solutionPart1(input):
    print(input)
    risk = findLeastRiskPathFrom(input, 0, 0)

    risk -= input[0][0]
    print("Risk: {}".format(risk))

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

