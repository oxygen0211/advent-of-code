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
                chars = [char for char in line.strip()]
                input.append(chars)
    return input


def solutionPart1(input):
    for sequence in input:
        for i in range(4, len(sequence)):
            subsequence = sequence[i-4:i]
            if len(set(subsequence)) >= 4:
                print(f"Found marker in sequence {sequence} at index {i}")
                break

def solutionPart2(input):
    for sequence in input:
        for i in range(4, len(sequence)):
            subsequence = sequence[i-14:i]
            if len(set(subsequence)) >= 14:
                print(f"Found marker in sequence {sequence} at index {i}")
                break

if __name__ == "__main__":
    part = int(sys.argv[1])
    inputfile = sys.argv[2]

    print("Solution {} for file {}".format(part, inputfile))

    input = readInput(inputfile)
    if part == 1:
        solutionPart1(input)

    else:
        solutionPart2(input)

