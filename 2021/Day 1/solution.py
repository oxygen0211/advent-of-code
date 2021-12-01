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
                input.append(int(line.strip()))
    return input

def solutionPart1(input):
    increase = 0

    for i in range(len(input)):
        if i == 0:
            print(input[i])
            continue;
    
        diff = input[i] - input[i - 1]

        if diff > 0:
            print("{} - increase".format(input[i]))
            increase += 1
        else:
            print(input[i])
        
    print("Answer: {}".format(increase))

def solutionPart2(input):
    sums = []
    for i in range(2, len(input)):
        sum = input[i] + input[i -1] + input[i -2]
        
        sums.append(sum)
    solutionPart1(sums)

if __name__ == "__main__":
    part = int(sys.argv[1])
    inputfile = sys.argv[2]

    print("Solution {} for file {}".format(part, inputfile))

    input = readInput(inputfile)
    if part == 1:
        solutionPart1(input)

    else:
        solutionPart2(input)

