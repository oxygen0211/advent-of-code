import sys
import math
from numpy import ones,vstack
from numpy.linalg import lstsq

def readInput(inputfile):
    input = []
    with open(inputfile) as file:
        lineFound = True

        while lineFound:
            line = file.readline()
            if not line:
                lineFound = False
            else:
                linedef = line.strip()
                input.append(linedef.split())
    return input

def buildVentLines(input):
    vents = []

    for line in input:
        start = line[0].split(',')
        end = line[2].split(',')

        vent = {
            "start": {
                "x": int(start[0]),
                "y": int(start[1])
            },
            "end": {
                "x": int(end[0]),
                "y": int(end[1])
            }
        }

        vents.append(vent)
    
    return vents

def filterVentLines(vents, diagonal=False):
    filtered = []
    for vent in vents:
        if vent["start"]["x"] == vent["end"]["x"] or vent["start"]["y"] == vent["end"]["y"]:
            filtered.append(vent)

    return filtered

def defineBoardSize(vents):
    boardX = 0
    boardY = 0

    print("Vents:")
    for vent in vents:
        if vent["start"]["x"] > boardX:
            boardX = vent["start"]["x"]
        
        if vent["end"]["x"] > boardX:
            boardX = vent["end"]["x"]

        if vent["start"]["y"] > boardY:
            boardY = vent["start"]["y"]
        
        if vent["end"]["y"] > boardY:
            boardY = vent["end"]["y"]
    boardX += 1
    boardY += 1
    return (boardX, boardY)

def createEmptyBoard(boardX, boardY):
    board = []
    
    for y in range(boardY):
        row = []
        for x in range(boardX):
            row.append('.')
        board.append(row)
    
    return board

def getMinMax(vent):
    minX = min(vent["start"]["x"], vent["end"]["x"])
    maxX = max(vent["start"]["x"], vent["end"]["x"])
    minY = min(vent["start"]["y"], vent["end"]["y"])
    maxY = max(vent["start"]["y"], vent["end"]["y"])

    return minX, minY, maxX, maxY

def buildBoard(vents, boardX, boardY):
    print("Board size: {}, {}".format(boardX, boardY))
    board = createEmptyBoard(boardX, boardY)

    for vent in vents:
        minX, minY, maxX, maxY = getMinMax(vent)

        print("min: {}, {}".format(minX, minY))
        print("max: {}, {}".format(maxX, maxY))
        
        for y in range(minY, maxY +1):
            for x in range(minX, maxX + 1):
                if board[y][x] == '.':
                    board[y][x] = 1

                else:
                    board[y][x] += 1
    for row in board:
        print(row)

    return board


def solutionPart1(input):
    vents = buildVentLines(input)
    vents = filterVentLines(vents)
    (boardX, boardY) = defineBoardSize(vents)
    board = buildBoard(vents, boardX, boardY)

    overlappingPoints = 0
    for row in board:
        for point in row:
            if not point == '.' and point >= 2:
                overlappingPoints += 1
    
    print("{} points are overlapping at least 2 lines".format(overlappingPoints))

def filterDiagonalVents(vents):
    filtered = []
    for vent in vents:
        diffx = vent["start"]["x"] - vent["end"]["x"]
        diffy = vent["start"]["y"] - vent["end"]["y"]
        angle = math.degrees(math.atan2(diffy, diffx))
        if abs(angle) == 45 or abs(angle) == 135 or abs(angle) == 225 or abs(angle) == 315: 
            print(angle)
            print("Including {} , {} -> {}, {} ".format(vent["start"]["x"], vent["start"]["y"], vent["end"]["x"], vent["end"]["y"]))
            print("diffX = {} diffY = {}".format(diffx, diffy))
            filtered.append(vent)
    return filtered

def getLinearCoefficients(vent):
    points = [(vent["start"]["x"],vent["start"]["y"]),(vent["end"]["x"],vent["end"]["y"])]
    x_coords, y_coords = zip(*points)
    A = vstack([x_coords,ones(len(x_coords))]).T
    m, c = lstsq(A, y_coords)[0]
    return round(m), round(c)

def appendDiagonalVents(vents, board):
    for vent in vents:
        minX, minY, maxX, maxY = getMinMax(vent)
        m, c = getLinearCoefficients(vent)
        print("{} m={}, c={}".format(vent, m, c))
        for x in range(minX, maxX + 1):
            y = int(math.floor(m * x + c)) - 1
            if board[y][x] == '.':
                board[y][x] = 1

            else:
                board[y][x] += 1
    
    for row in board:
        print(row)

    return board
def solutionPart2(input):
    vents = buildVentLines(input)
    straightVents = filterVentLines(vents)
    diagonalVents = filterDiagonalVents(vents)

    combinedVents = []
    combinedVents.extend(straightVents)
    combinedVents.extend(diagonalVents)
    boardX, boardY = defineBoardSize(combinedVents)

    board = buildBoard(straightVents, boardX, boardY)

    board = appendDiagonalVents(diagonalVents, board)

    overlappingPoints = 0
    for row in board:
        for point in row:
            if not point == '.' and point >= 2:
                overlappingPoints += 1
    
    print("{} points are overlapping at least 2 lines".format(overlappingPoints))

if __name__ == "__main__":
    part = int(sys.argv[1])
    inputfile = sys.argv[2]

    print("Solution {} for file {}".format(part, inputfile))

    input = readInput(inputfile)
    if part == 1:
        solutionPart1(input)

    else:
        solutionPart2(input)

