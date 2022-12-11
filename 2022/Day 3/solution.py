from os import error
import sys

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def readInput(inputfile):
    input = []
    with open(inputfile) as file:
        lineFound = True

        while lineFound:
            line = file.readline()
            if not line:
                lineFound = False
            else:
                line = [char for char in line.strip()]
                input.append(line)

    return input

def solutionPart1(input):
    score = 0
    for rucksack in input:
        compartment_size = int(len(rucksack) / 2)
        compartment_1 = rucksack[:compartment_size]
        compartment_2 = rucksack[compartment_size:]
        for item in compartment_1:
            if item in compartment_2:
                score += alphabet.index(item) + 1
                break

    print(f"priorities sum: {score}")

def solutionPart2(input):
    score = 0

    chunk_size = 3
    groups = [input[i:i + chunk_size] for i in range(0, len(input), chunk_size)]

    for group in groups:
        print(group)
        for item in group[0]:
            if item in group[1] and item in group [2]:
                score += alphabet.index(item) + 1
                break
    
    print(f"priorities sum: {score}")

if __name__ == "__main__":
    part = int(sys.argv[1])
    inputfile = sys.argv[2]

    print("Solution {} for file {}".format(part, inputfile))

    input = readInput(inputfile)
    if part == 1:
        solutionPart1(input)

    else:
        solutionPart2(input)

