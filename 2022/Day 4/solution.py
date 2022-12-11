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
                line = line.strip()
                sections = []
                for section in line.split(','):
                    sections.append([int(x) for x in section.split("-")])
                input.append(sections)

    return input

def solutionPart1(input):
    print(input)
    full_overlaps = 0
    for pair in input:
        if pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]:
            print(f"pair {pair[0]} and {pair[1]} fully overlap")
            full_overlaps += 1

        elif pair[1][0] >= pair[0][0] and pair[1][1] <= pair[0][1]:
            print(f"pair {pair[0]} and {pair[1]} fully overlap")
            full_overlaps += 1

    print(f"found {full_overlaps} fully overlapping pairs")


def solutionPart2(input):
    print(input)
    overlaps = 0
    for pair in input:
        if pair[1][0] >= pair[0][0] and pair[1][0] <= pair[0][1]:
            print(f"pair {pair[0]} and {pair[1]} overlap")
            overlaps += 1

        elif pair[0][0] >= pair[1][0] and pair[0][0] <= pair[1][1]:
            print(f"pair {pair[0]} and {pair[1]} overlap")
            overlaps += 1

    print(f"found {overlaps} overlapping pairs")

if __name__ == "__main__":
    part = int(sys.argv[1])
    inputfile = sys.argv[2]

    print("Solution {} for file {}".format(part, inputfile))

    input = readInput(inputfile)
    if part == 1:
        solutionPart1(input)

    else:
        solutionPart2(input)

