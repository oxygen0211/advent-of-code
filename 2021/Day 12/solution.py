from os import error
import sys
from collections import Counter

def readInput(inputfile):
    input = []
    with open(inputfile) as file:
        lineFound = True

        while lineFound:
            line = file.readline()
            if not line:
                lineFound = False
            else:
                path = line.strip().split("-")
                input.append({"start": path[0], "end": path[1]})
    return input

def searchPaths(path, connections, maxSmallCaveVisits):
    print("Extending path {}".format(path))
    paths = []
    start = path[len(path) - 1]
    for con in connections:
        segment = []
        if con["start"] == start:
            segment = [start, con["end"]]
        if con["end"] == start:
            segment = [start, con["start"]]
        
        if len(segment) > 0:
            newPath = path.copy()
            newPath.extend(segment[1:])
            
            smallCaveVisits = {}
            for cave in newPath:
                if cave.islower():
                    if not cave in smallCaveVisits:
                        smallCaveVisits[cave] = 1
                    else:   
                        smallCaveVisits[cave] += 1

            withinSmallCaveBounds = True
            multiVisits = 0
            for visit in smallCaveVisits.values():
                withinSmallCaveBounds = withinSmallCaveBounds and visit <= maxSmallCaveVisits
                if visit > 1:
                    multiVisits += 1

            if withinSmallCaveBounds:
                if maxSmallCaveVisits > 1:
                    if multiVisits <= 1:
                        paths.append(newPath)
                else:    
                    paths.append(newPath)
    
    extendedPaths = []
    for path in paths:
        lastCave = path[len(path)-1]
        if lastCave == "start":
            continue
        if lastCave == "end":
            extendedPaths.append(path)
            continue
        
        followingPaths = searchPaths(path, connections, maxSmallCaveVisits)
        extendedPaths.extend(followingPaths)
            
    return extendedPaths

def solutionPart1(input):
    paths = searchPaths(["start"], input, 1)

    for path in paths:
        print(path)

    print("Found {} valid paths.".format(len(paths)))

def solutionPart2(input):
    print("Finding all available paths...")
    paths = searchPaths(["start"], input, 2)

    print("Found {} valid paths.".format(len(paths)))

if __name__ == "__main__":
    part = int(sys.argv[1])
    inputfile = sys.argv[2]
    

    print("Solution {} for file {}".format(part, inputfile))

    input = readInput(inputfile)
    if part == 1:
        solutionPart1(input)

    else:
        solutionPart2(input)

