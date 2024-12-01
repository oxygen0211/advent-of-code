from os import error
import sys

def readInput(inputfile):
    input = []
    with open(inputfile) as file:
        lineFound = True
        while lineFound:
            line = file.readline()
            if not line:
                lineFound = False
            else:
                row = [int(c) for c in line.strip()]
                input.append(row)
    return input

def solutionPart1(input):
    visible = 0

    for row in input:
        print(row)

    for y, row in enumerate(input):
        for x, height in enumerate(row):
            if x < 1:
                visible += 1
                continue

            if x >= len(row) - 1:
                visible += 1
                continue

            if y < 1:
                visible += 1
                continue

            if y >= len(row) - 1:
                visible += 1
                continue

            visible_left = True
            for xc in range(x):
                if row[xc] >= height:
                    visible_left = False
            
            visible_right = True
            for xc in range(x + 1, len(row)):
                if row[xc] >= height:
                    visible_right = False
            
            visible_top = True
            for yc in range(y):
                if input[yc][x] >= height:
                    visible_top = False
            
            visible_bottom = True
            for yc in range(y + 1, len(input)):
                if input[yc][x] >= height:
                    visible_bottom = False

            if not visible_left and not visible_right and not visible_top and not visible_bottom:
                print(f"{x}, {y} is visible")
                visible += 1
    
    print(f"visible trees: {visible}")

def solutionPart2(input):
    for row in input:
        print(row)

if __name__ == "__main__":
    part = int(sys.argv[1])
    inputfile = sys.argv[2]

    print("Solution {} for file {}".format(part, inputfile))

    input = readInput(inputfile)
    if part == 1:
        solutionPart1(input)

    else:
        solutionPart2(input)

