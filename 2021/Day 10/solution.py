from os import error
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
                input.append(line.strip())
    return input

errorScores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

completerScores = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

chunkOpeners = ['(', "[", "{", "<"]
chunkClosers = {
    '(': ")", 
    "[": "]", 
    "{": "}", 
    "<": ">"
}

def isLineCorrupt(line):
    chunkStack = []

    for char in line:
        if char in chunkOpeners:
            chunkStack.append(char)
            continue
            
        opener = chunkStack.pop()
        if not char == chunkClosers[opener]:
            return char
    
    return ''

def solutionPart1(input):
    score = 0
    for line in input:
        corruptChar = isLineCorrupt(line)
        if not corruptChar == '':
            print("Corrupt line found! {}".format(line))
            score += errorScores[corruptChar]
    
    print("Overall error score: {}".format(score))


def solutionPart2(input):
    scores = []
    nonCorrupt = []
    for line in input:
        corruptChar = isLineCorrupt(line)
        if corruptChar == '':
            nonCorrupt.append(line)
    
    for line in nonCorrupt:
        chunkStack = []

        for char in line:
            if char in chunkOpeners:
                chunkStack.append(char)
                continue
            
            opener = chunkStack.pop()
            if not chunkClosers[opener] == char:
                raise error("Error: Expected closing character does not match Got {}, excpeted {}".format(char, opener))

        print("Incomplete section: {}".format(chunkStack))
        completion = []
        score = 0
        while len(chunkStack) > 0:
            char = chunkStack.pop()
            closer = chunkClosers[char]
            completion.append(closer)
            score = score * 5 + completerScores[closer]
        
        scores.append(score)
        
        print("Required for completion: {}".format(completion))
        print("Line score: {}".format(score))

    scores.sort()
    print("Scores: {}".format(scores))
    middle = math.floor(len(scores) / 2)
    print("Middle score (index {}): {}".format(middle, scores[middle]))

if __name__ == "__main__":
    part = int(sys.argv[1])
    inputfile = sys.argv[2]

    print("Solution {} for file {}".format(part, inputfile))

    input = readInput(inputfile)
    if part == 1:
        solutionPart1(input)

    else:
        solutionPart2(input)

