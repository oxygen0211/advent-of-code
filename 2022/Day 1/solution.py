from os import error
import sys

def readInput(inputfile):
    input = []
    elf_food = []
    with open(inputfile) as file:
        lineFound = True

        while lineFound:
            line = file.readline()
            if not line:
                lineFound = False
            else:
                line = line.strip()

                if not line:
                    input.append(elf_food)
                    elf_food = []

                else:
                    elf_food.append(int(line))

    input.append(elf_food)
    return input

def solutionPart1(input):
    print(input)

    max_cals = 0
    max_index = 0

    for i, elf in enumerate(input):
        elf_cals = 0
        for cals in elf:
            elf_cals += cals
        
        if elf_cals >= max_cals:
            max_cals = elf_cals
            max_index = i

    print(f"Elf {max_index} has most calories ({max_cals})")


def solutionPart2(input):
    print(input)

    totals = []
    for elf in input:
        elf_cals = 0
        for cals in elf:
            elf_cals += cals
        totals.append(elf_cals)

    totals.sort(reverse=True)
    print(totals)

    top_sum = totals[0] + totals[1] + totals[2]

    print(f"Sum of top 3: {top_sum}")

if __name__ == "__main__":
    part = int(sys.argv[1])
    inputfile = sys.argv[2]

    print("Solution {} for file {}".format(part, inputfile))

    input = readInput(inputfile)
    if part == 1:
        solutionPart1(input)

    else:
        solutionPart2(input)

