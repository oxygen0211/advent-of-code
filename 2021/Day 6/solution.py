import sys
import math

def readInput(inputfile):
    input = []
    with open(inputfile) as file:
        lineFound = True

        while lineFound:
            line = file.readline()
            if not line:
                lineFound = False
            else:
                startingPoints = line.strip().split(',')
                input.append([int(i) for i in startingPoints])
    return input

def solutionPart1(input, epochs):
    fish = input[0]
    print("Initial: {}".format(fish))
    for day in range(1, epochs + 1):
        for i in range(len(fish)):
            if fish[i] == 0:
                fish.append(8)
                fish[i] = 6
                continue

            fish[i] -= 1
    
        print("After day {}: {}".format(day, fish))

    print("After {} days, there will be {} fish".format(epochs, len(fish)))

def reproduceBroken(epoch, childrenAtEpoch, maxEpochs):
    if epoch > maxEpochs:
        return childrenAtEpoch
    
    if not epoch in childrenAtEpoch:
        childrenAtEpoch[epoch] = 1
    else:
        childrenAtEpoch[epoch] += 1
        
    nextRepro = epoch + 6
    while not nextRepro >= maxEpochs:
        if not nextRepro in childrenAtEpoch:
            childrenAtEpoch[nextRepro] = 1
        else:
            childrenAtEpoch[nextRepro] += 1
        
        childrenAtEpoch = reproduce(nextRepro + 8, childrenAtEpoch, maxEpochs)
        nextRepro += 6
    
    return childrenAtEpoch

def reproduce(epoch, maxEpochs):
    newChildren = []
    while epoch < maxEpochs:
        newChildren.append(epoch)
        epoch += 6
    return newChildren

def getChildSum(fishes, epochs):
    startingEpochs = {}
    sum = 0
    for fish in fishes:
        if not (fish + 1) in startingEpochs:
            startingEpochs[fish + 1] = 1
        else:
            startingEpochs[fish + 1] += 1
    print(fishes)
    print(startingEpochs)
    reproEpochs = []
    sum = 0
    for epoch in startingEpochs.keys():
        childEpochs = []
        for e in reproduce(epoch, epochs):
            firstRepro = e + 8
            if firstRepro <= epochs:
                childEpochs.append(e)
        amount = startingEpochs[epoch]
        sum += len(childEpochs) * amount
        reproEpochs.extend(childEpochs * amount)
    print("sum {}, repros {}".format(sum, len(reproEpochs)))
    if len(reproEpochs) > 0:
        sum += getChildSum(reproEpochs, epochs)
    return sum

def solutionPart2(input, epochs):
    initialfish = input[0]
    fish = [0 for _ in range(7)]
    newfish = [0 for _ in range(7)]

    for f in initialfish:
        fish[f] += 1
    
    total = sum(fish)

    day = 0
    while day < epochs:
        d = day % 7
        d2 = (day+2) % 7

        total += fish[d]
        newfish[d2] = fish[d]

        fish[d] += newfish[d]

        day += 1
    #sum = len(fish)
    
    #sum += getChildSum(fish, epochs)
    
    print("{} fish will be produced after {} days".format(total, epochs))

if __name__ == "__main__":
    part = int(sys.argv[1])
    inputfile = sys.argv[2]
    epochs = int(sys.argv[3])

    print("Solution {} for file {}".format(part, inputfile))

    input = readInput(inputfile)
    if part == 1:
        solutionPart1(input, epochs)

    else:
        solutionPart2(input, epochs)

