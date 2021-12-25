from os import error
import sys

conversionTable = {
    '#': 1,
    '.': 0
}

def readInput(inputfile):
    input = {}
    with open(inputfile) as file:
        lineFound = True

        lineCount = 0
        while lineFound:
            line = file.readline()
            if not line:
                lineFound = False
            else:
                line = line.strip()
                if not "filter" in input:
                    input["filter"] = line
                    continue
                
                if line == "":
                    continue

                if not "image" in input:
                    input["image"] = []

                input["image"].append(line)

            lineCount += 1
    return input

def solutionPart1(input, steps):
    print(input)
    image = input["image"]
    for step in range(steps):
        newImage = []
        for y in range(len(image)):
            newRow = ['.' for _ in image]
            for x in range(len(image[y])):
                binaryIndex = ""
                for x1 in range(x -1, x + 2):
                    for y1 in range(y -1, y + 2):
                        if x1 < 0 or y1 < 0 or y1 > len(image) - 1 or x1 > len(image[y1]) - 1:
                            binaryIndex += "0"
                            continue
                        else:
                            char = image[y1][x1]
                            binaryIndex += str(conversionTable[char])
                index = int(binaryIndex, 2)
                print("Binary index for {}, {}: {} -> {}".format(x, y, binaryIndex, index))
                newRow[x] = input["filter"][index]
            newImage.append(newRow)
        image = newImage
        print(image)
    for row in image:
        print(row)
    




def solutionPart2(input):
    print(input)

if __name__ == "__main__":
    part = int(sys.argv[1])
    inputfile = sys.argv[2]
    steps = int(sys.argv[3])

    print("Solution {} for file {}".format(part, inputfile))

    input = readInput(inputfile)
    if part == 1:
        solutionPart1(input, steps)

    else:
        solutionPart2(input)

