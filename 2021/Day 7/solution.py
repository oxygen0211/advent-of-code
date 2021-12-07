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
                startingPoints = line.strip().split(',')
                input.append([int(i) for i in startingPoints])
    return input

def solutionPart1(input):
    positions = input[0]
    highestPos = max(positions)

    bestPos = 0
    bestFuel = -1
    for i in range(highestPos + 1):
        fuelSum = 0
        for pos in positions:
            fuelSum += abs(pos - i)

        if bestFuel < 0 or fuelSum < bestFuel:
            bestFuel = fuelSum
            bestPos = i
    
    print("Best final position is {}, requiring {} fuel".format(bestPos, bestFuel))
        


def solutionPart2(input):
    positions = input[0]
    highestPos = max(positions)

    bestPos = 0
    bestFuel = -1
    for i in range(highestPos + 1):
        fuelSum = 0
        for pos in positions:
            positionFuel = 0
            requiredSteps = abs(pos - i)
            for j in range(1, requiredSteps + 1):
                positionFuel += j
            
            fuelSum += positionFuel
            
            print("{} to {}: {} Fuel".format(pos, i, positionFuel))

        if bestFuel < 0 or fuelSum < bestFuel:
            bestFuel = fuelSum
            bestPos = i
    
    print("Best final position is {}, requiring {} fuel".format(bestPos, bestFuel))
        

if __name__ == "__main__":
    part = int(sys.argv[1])
    inputfile = sys.argv[2]

    print("Solution {} for file {}".format(part, inputfile))

    input = readInput(inputfile)
    if part == 1:
        solutionPart1(input)

    else:
        solutionPart2(input)

