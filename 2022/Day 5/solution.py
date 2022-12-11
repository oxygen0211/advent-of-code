from os import error
import sys

def readInput(inputfile):
    input = {
        'stacks': {},
        'instructions': []
    }
    with open(inputfile) as file:
        lineFound = True
        while lineFound:
            line = file.readline()
            if not line:
                lineFound = False
            else:
                chars = [char for char in line]
                print(line)
                for i, char in enumerate(chars):
                    if char == "[":
                        item = line[i+1]
                        stack = int((i+1) / 4)
                        if not stack in input['stacks']:
                            input['stacks'][stack] = []

                        input['stacks'][stack].append(item)
                
                if line.startswith("move"):
                    instructions = line.strip().split(" ")
                    instruction = {
                        'amount': int(instructions[1]),
                        'from': int(instructions[3]) - 1,
                        'to': int(instructions[5]) - 1
                    }
                    input['instructions'].append(instruction)

        for stack in input['stacks']:
            input['stacks'][stack].reverse()

        input["stacks"] = dict(sorted(input["stacks"].items()))

    return input


def determine_top_section(input):
    top_sequence = []
    for stack, value in input["stacks"].items():
        top_sequence.append(value[-1])

    return ''.join(top_sequence)

def solutionPart1(input):
    print(input)

    for instruction in input['instructions']:
        for i in range(0, instruction["amount"]):
            crate = input["stacks"][instruction["from"]].pop()
            input["stacks"][instruction["to"]].append(crate)
        
        print(f"executed step {instruction}")
        print(input["stacks"])
    
    print(f"top sequence: {determine_top_section(input)}")

def solutionPart2(input):
    for instruction in input['instructions']:
        pop_index = 0 - instruction["amount"]
        crates = input["stacks"][instruction["from"]][pop_index:]
        input["stacks"][instruction["from"]] = input["stacks"][instruction["from"]][:pop_index]
        input["stacks"][instruction["to"]].extend(crates)
        
        print(f"executed step {instruction}")
        print(input["stacks"])
    
    print(f"top sequence: {determine_top_section(input)}")

if __name__ == "__main__":
    part = int(sys.argv[1])
    inputfile = sys.argv[2]

    print("Solution {} for file {}".format(part, inputfile))

    input = readInput(inputfile)
    if part == 1:
        solutionPart1(input)

    else:
        solutionPart2(input)

