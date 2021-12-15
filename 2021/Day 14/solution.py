from os import error
import sys
from collections import Counter

def readInput(inputfile):
    input = {
        "start": "",
        "replacements": {}
    }
    with open(inputfile) as file:
        lineFound = True

        while lineFound:
            line = file.readline()
            if not line:
                lineFound = False
            else:
                line = line.strip()
                if "->" in line:
                    inst = line.split("->")
                    pattern = inst[0].strip()
                    insert = inst[1].strip()
                    input["replacements"][pattern] = insert
            
                else:
                    if len(line) > 0:
                        input["start"] = line.strip()
    return input

def count(currentString):
    occurences = {}
    for c in currentString:
        if not c in occurences:
            occurences[c] = 1
        else:
            occurences[c] += 1

    leastOccurence = -1
    mostOccurence = 0
    for c in occurences:    
        if leastOccurence < 0 or occurences[c] < leastOccurence:
            leastOccurence = occurences[c]
        
        if occurences[c] > mostOccurence:
            mostOccurence = occurences[c]

    return leastOccurence, mostOccurence

def solutionPart1(input, steps):
    currentString = [c for c in input["start"]]
    currentStep = 0
    while currentStep < steps:
        print("Calculating step {}".format(currentStep))
        newString = currentString[:1]
        
        for i in range(len(currentString)):
            if i < len(currentString) - 1:
                char1 = currentString[i]
                char2 = currentString[i+1]

                insert = input["replacements"][char1 + char2]
                newString.append(insert)
                newString.append(char2)

        currentString = newString
        currentStep += 1
    
    print("Final String (length {}):".format(len(currentString)))
    print(currentString)
    
    leastOccurence, mostOccurence = count(currentString)

    print("{} - {} = {}".format(mostOccurence, leastOccurence, mostOccurence - leastOccurence))

def solutionPart2(input, steps):
    currentString = input["start"]
    
    currentStep = 0
    while currentStep < steps:
        print("Calculating step {}".format(currentStep))
        
        lastReplacedIndex = -100
        for replacement in input["replacements"]:
            searchString = replacement
            replacement = searchString[0] + input["replacements"][searchString] + searchString[1]

            if searchString in currentString:
                index = currentString.index(searchString)
                if abs(index - lastReplacedIndex) < 2:
                    continue

                pre = currentString[:index]
                post = currentString[index + 2:]

                currentString = pre + replacement + post
                lastReplacedIndex = index    
        
        #print(replaceSteps)
        #replaceIndexes = sorted(replaceSteps)
        #lastReplacedIndex = 0
        #for i in range(len(replaceIndexes)):
        #    index = replaceIndexes[i]
        #    if i > 0 and index - lastReplacedIndex < 2:
        #        continue
            
        #    pre = currentString[:index]
        #    replacement = replaceSteps[index]
        #    post = currentString[index + 2:]

        #    print("Building {} - {} - {} at index {}".format(pre, replacement, post, index))
        #    currentString = pre + replacement + post
        #    lastReplacedIndex = index    

            print("New String: {}".format(currentString))
        currentStep += 1

    leastOccurence, mostOccurence = count(currentString)

    print("{} - {} = {}".format(mostOccurence, leastOccurence, mostOccurence - leastOccurence))

if __name__ == "__main__":
    part = int(sys.argv[1])
    inputfile = sys.argv[2]
    steps = int(sys.argv[3])
    

    print("Solution {} for file {}".format(part, inputfile))

    input = readInput(inputfile)
    if part == 1:
        solutionPart1(input, steps)

    else:
        solutionPart2(input, steps)

