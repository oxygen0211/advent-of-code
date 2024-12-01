from os import error
import sys

def readInput(inputfile):
    input = {
        "list1": [],
        "list2": []
    }
    with open(inputfile) as file:
        lineFound = True

        while lineFound:
            line = file.readline()
            if not line:
                lineFound = False
            else:
                combination = line.strip().split()
                input["list1"].append(int(combination[0]))
                input["list2"].append(int(combination[1]))
    return input

def solutionPart1(input):
    print(input)
    total_score = 0

    input["list1"].sort()
    input["list2"].sort()

    for i in range(0, len(input["list1"])):
        idList1 = input["list1"][i]
        idList2 = input["list2"][i]
        distance = abs(idList2 - idList1)
        total_score += distance

    print(f"Total distance is {total_score}")


def solutionPart2(input):
    print(input)
    total_score = 0

    input["list1"].sort()
    input["list2"].sort()

    for id in input["list1"]:
        count = 0
        for id2 in input["list2"]:
            if id == id2:
                count += 1
        
        similarity = id * count
        total_score += similarity

    print(f"Total distance is {total_score}")


if __name__ == "__main__":
    part = int(sys.argv[1])
    inputfile = sys.argv[2]

    print("Solution {} for file {}".format(part, inputfile))

    input = readInput(inputfile)
    if part == 1:
        solutionPart1(input)

    else:
        solutionPart2(input)

