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
                line = line.strip()
                inout = line.split("|")
                pattern = {
                    "input": inout[0].split(" ")[:-1],
                    "output": inout[1].split(" ")[1:]
                }

                input.append(pattern)
    return input

numberByLength = {
    2: [1],
    3: [7],
    4: [4],
    5: [2, 3, 5],
    6: [0, 6, 9],
    7: [8]
}

def solutionPart1(input):
    print(input)
    uniques = 0
    for pattern in input:
        for num in pattern["output"]:
            possibleNums = numberByLength[len(num)]
            if len(possibleNums) == 1:
                determined = possibleNums[0]
                print("{} = {}".format(num, determined))
                uniques += 1

    print("Found {} unique number patterns".format(uniques))


def solutionPart2(input):
    segments = ["-" for _ in range(7)]
    allDecoded = False
    while not allDecoded:
        for pattern in input:
            nums = [{"num": n} for n in pattern["output"]]
        
            for i in range(len(nums)):
                num = nums[i]
                encoded = num["num"]
                possibleNums = numberByLength[len(encoded)]
                if len(possibleNums) == 1:
                    determined = possibleNums[0]
                    num["dec"] = determined
            
            print(nums)


if __name__ == "__main__":
    part = int(sys.argv[1])
    inputfile = sys.argv[2]

    print("Solution {} for file {}".format(part, inputfile))

    input = readInput(inputfile)
    if part == 1:
        solutionPart1(input)

    else:
        solutionPart2(input)

