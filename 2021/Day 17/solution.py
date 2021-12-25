from os import error
import sys
import math

def parseAxisDefinition(defString):
    borders = [int(n) for n in defString.split("..")]
    minimum = min(borders)
    maximum = max(borders)

    return [minimum, maximum]

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

                targetDef = line[len("target area: "):].split(",")

                target = {}
                for definition in targetDef:
                    axis = definition.strip()[:1]
                    definitionString = definition.strip()[2:]
                    target[axis] = parseAxisDefinition(definitionString)
                
                input.append(target)

    return input

def checkTargetHit(position, targetDef):
    if position[0] < targetDef["x"][0]:
        return False
    if position[0] > targetDef["x"][1]:
        return False 
    if position[1] < targetDef["y"][0]:
        return False
    if position[1] > targetDef["y"][1]:
        return False

    return True

def simulate(xVelocity, yVelocity, targetDef):
    overshot = False
    underShotY = False
    targetHit = False

    position = [0, 0]
    print("Simulating shot with velocity {}, {} from {} with a target of {}".format(xVelocity, yVelocity, position, targetDef))
    currentXVelocity = xVelocity
    currentYvelocity = yVelocity
    yMax = -1000
    while not overshot and not underShotY and not targetHit:
        position[0] = position[0] + currentXVelocity
        position[1] = position[1] + currentYvelocity

        if position[1] > yMax:
            yMax = position[1]

        if abs(currentXVelocity) > 0:
            currentXVelocity -= 1
        
        currentYvelocity -= 1

        overshot = position[0] > targetDef["x"][1]
        underShotY = position[1] < targetDef["y"][0]
        targetHit = checkTargetHit(position, targetDef)

        print("New Point {}, new Velocity: {}, {}. Target Hit? {}. Overshot X? {}. Undershot Y? {}".format(position, currentXVelocity, currentYvelocity, targetHit, overshot, underShotY))

    return overshot, targetHit, yMax
def solutionPart1(input):
    print(input)

    for targetDef in input:
        successfullVelocities = []
        for xVelocity in range(1, targetDef["x"][1] + 1):
            reachableX = 0
            for n in range(xVelocity + 1):
                reachableX += n
            if reachableX <= targetDef["x"][0] + 1:
                print("Maximum reachable X of {} is {}. Cannot reach minimum X of {} with that".format(xVelocity, reachableX, targetDef["x"][0]))
                continue
            yVelocity = targetDef["y"][0]
            overshot = False
            while yVelocity < 10 and not overshot:
                overshot, targetHit, yMax = simulate(xVelocity, yVelocity, targetDef)
                if targetHit:
                    print("Successfull target Hit with {}, {}".format(xVelocity, yVelocity))
                    successfullVelocities.append({"x": xVelocity, "y": yVelocity, "yMax": yMax})
                yVelocity += 1

        print("Successfull velocities:")

        maxY = -1000
        bestX = 0
        bestY = 0
        for velocity in successfullVelocities:
            if velocity["yMax"] > maxY:
                print(velocity)
                maxY = velocity["yMax"]
                bestY = velocity["y"]
                bestX = velocity["x"]
        
        print("Highest Y({}) with velocity {}, {}".format(maxY, bestX, bestY))



def solutionPart2(input):
    print(input)

if __name__ == "__main__":
    part = int(sys.argv[1])
    inputfile = sys.argv[2]
    

    print("Solution {} for file {}".format(part, inputfile))

    input = readInput(inputfile)
    if part == 1:
        solutionPart1(input)

    else:
        solutionPart2(input)

