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
                command = line.strip()
                input.append(command.split())
    return input

def solutionPart1(input):
    horizontal = 0
    vertical = 0

    for command in input:
        instruction = command[0]
        amount = int(command[1])

        if instruction == "forward":
            horizontal += amount
        
        if instruction == "down":
            vertical += amount

        if instruction == "up":
            vertical -= amount

    print("Horizontal: {}".format(horizontal))
    print("Vertical: {}".format(vertical))
    print("Answer: {}".format(horizontal * vertical))

def solutionPart2(input):
    horizontal = 0
    vertical = 0
    aim = 0

    for command in input:
        instruction = command[0]
        amount = int(command[1])

        if instruction == "forward":
            horizontal += amount
            vertical += aim * amount
        
        if instruction == "down":
            aim += amount

        if instruction == "up":
            aim -= amount

    print("Horizontal: {}".format(horizontal))
    print("Vertical: {}".format(vertical))
    print("Answer: {}".format(horizontal * vertical))

if __name__ == "__main__":
    part = int(sys.argv[1])
    inputfile = sys.argv[2]

    print("Solution {} for file {}".format(part, inputfile))

    input = readInput(inputfile)
    if part == 1:
        solutionPart1(input)

    else:
        solutionPart2(input)

