from os import error
import sys
from collections import Counter

def readInput(inputfile):
    input = {
        "dots": [],
        "instructions": [],
        "xmax": 0,
        "ymax": 0
    }
    with open(inputfile) as file:
        lineFound = True

        while lineFound:
            line = file.readline()
            if not line:
                lineFound = False
            else:
                line = line.strip()
                if line.startswith("fold"):
                    foldInst = line[11:].split("=")
                    input["instructions"].append({"axis": foldInst[0], "index": int(foldInst[1])})
            
                else:
                    if len(line) > 0:
                        point = line.split(",")
                        x = int(point[0])
                        y = int(point[1])
                        input["dots"].append({"x": x, "y": y})
                        if x > input["xmax"]:
                            input["xmax"] = x
                        
                        if y > input["ymax"]:
                            input["ymax"] = y
    return input

def foldX(index, field):
    foldedField = []

    for row in field:
        baseRow = row[:index]
        mirrorRow = row[index+1:]
        lastBaseIndex = len(baseRow) - 1

        for x in range(len(mirrorRow)):
            foldIndex = lastBaseIndex - x
            if mirrorRow[x] == "#":
                baseRow[foldIndex] = mirrorRow[x]
        
        foldedField.append(baseRow)

    return foldedField

def foldY(index, field):
    baseField = field[:index]
    lastBaseIndex = len(baseField) - 1

    foldedField = field[index+1:]
    for y in range(len(foldedField)):
        row = foldedField[y]
        foldIndex = lastBaseIndex - y

        for x in range(len(row)):
            if row[x] == "#":
                baseField[foldIndex][x] = row[x]

    return baseField

def fold(axis, index, field):
    print("Folding at {} axis on index {}".format(axis, index))

    if axis == "x":
        return foldX(index, field)
    
    if axis == "y":
        return foldY(index, field)
    return field

def solutionPart1(input):
    field = [['.' for _ in range(input["xmax"] + 1)] for _ in range(input["ymax"] + 1)]
    for dot in input["dots"]:
        field[dot["y"]][dot["x"]] = "#"

    instruction = input["instructions"][0]
    field = fold(instruction["axis"], instruction["index"], field)
    
    visibleDots = 0
    for row in field:
        print(row)
        visibleDots += row.count("#")
    
    print("There are {} visible dots in the folded sheet".format(visibleDots))

def solutionPart2(input):
    field = [['.' for _ in range(input["xmax"] + 1)] for _ in range(input["ymax"] + 1)]
    for dot in input["dots"]:
        field[dot["y"]][dot["x"]] = "#"

    instruction = input["instructions"][0]
    for instruction in input["instructions"]:
        field = fold(instruction["axis"], instruction["index"], field)
        print("New Field:")
    
    visibleDots = 0

    print("Code:")
    for row in field:
        minimalizedRow = ""
        for dot in row:
            minimalizedRow += dot
            minimalizedRow += " "
        print(minimalizedRow)
        visibleDots += row.count("#")

if __name__ == "__main__":
    part = int(sys.argv[1])
    inputfile = sys.argv[2]
    

    print("Solution {} for file {}".format(part, inputfile))

    input = readInput(inputfile)
    if part == 1:
        solutionPart1(input)

    else:
        solutionPart2(input)

