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
                bits = []
                for char in [*line.strip()]:
                    bits.append(int(char))
                input.append(bits)
                
    return input

def solutionPart1(input):
    gamma = ''
    epsilon = ''

    for i in range(len(input[0])):
        ones = 0
        zeroes = 0
        for val in input:
            if val[i] == 1:
                ones += 1  
            else:
                zeroes += 1
        
        if ones > zeroes:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    
    gammadec = int(gamma, 2)
    epsilondec = int(epsilon, 2)

    print("Gamma: {} = {}".format(gamma, gammadec))
    print("Epsilon: {} = {}".format(epsilon, epsilondec))

    print("Answer: {}".format(gammadec * epsilondec))

def stripValues(remainingValues, i, requiredBitVal):
    stripped = []

    for val in remainingValues:
        if val[i] == requiredBitVal:
            stripped.append(val)

    return stripped

def getRating(comparer, input):
    remainingValues = input
    for i in range(len(input[0])):
        ones = 0
        zeroes = 0
        for val in remainingValues:
            if val[i] == 1:
                ones += 1  
            else:
                zeroes += 1

        requiredBitVal = 0
        if comparer == "most":
            requiredBitVal = 1 if ones >= zeroes else 0
        
        if comparer == "least":
            requiredBitVal = 1 if ones < zeroes else 0

        remainingValues = stripValues(remainingValues, i, requiredBitVal)
        if len(remainingValues) == 1:
            return remainingValues[0]

    return remainingValues[0]

def solutionPart2(input):
    oxygenRating = getRating("most", input)
    oxygenDec = int("".join(str(i) for i in oxygenRating), 2)
    print("oxygen: {} = {}".format(oxygenRating, oxygenDec))
    
    co2Rating = getRating("least", input)
    co2Dec = int("".join(str(i) for i in co2Rating), 2)
    print("co2: {} = {}".format(co2Rating, co2Dec))

    print("Answer: {}".format(oxygenDec * co2Dec))

if __name__ == "__main__":
    part = int(sys.argv[1])
    inputfile = sys.argv[2]

    print("Solution {} for file {}".format(part, inputfile))

    input = readInput(inputfile)
    if part == 1:
        solutionPart1(input)

    else:
        solutionPart2(input)

