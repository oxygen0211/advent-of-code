from os import error
import sys
import binascii

mappings = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101', 
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}

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
                conversion = ''
                for c in line:
                    conversion += mappings[c]

                input.append(conversion)
    return input

def solutionPart1(input):
    print(input)
    versionSum = 0
    for packet in input:
        version = int(packet[:3], 2)
        print("Version: {}".format(version))
        typeId = int(packet[3:6], 2)
        print("Type: {}".format(typeId))

        versionSum += version
    
    print("Version sum: {}".format(versionSum))

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

