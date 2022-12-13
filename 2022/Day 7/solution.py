from os import error
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
                command = line.split()
                input.append(command)
    return input

def calcualte_size_small(dir):
    size = 0
    if "directories" in dir:
        for name in dir["directories"]:
            size += calcualte_size_small(dir["directories"][name])
        
        if "size" in dir and dir["size"] <= 100000:
            size += dir["size"]
    return size

def build_dir_map(input):
    directories = {"directories": {}}
    current_path = []
    for line in input:
        if line[0] == "$":
            if line[1] == "cd":
                if line[2] == "..":
                    current_path.pop()
                else:
                    current_path.append(line[2])
        if line[0].isdigit():
            size = int(line[0])
            
            dir_info = directories
            for dir in current_path:
                if not dir in dir_info["directories"]:
                    dir_info["directories"][dir] = {"size": 0, "directories": {}}
                
                dir_info = dir_info["directories"][dir]
                dir_info["size"] += size

    return directories

def solutionPart1(input):
    directories = build_dir_map(input)
            
    overall_size = calcualte_size_small(directories)

    print(f"overall size is {overall_size}")

def calcualte_size(dir):
    size = dir["size"] if "size" in dir else 0
    if "directories" in dir:
        for name in dir["directories"]:
            size += calcualte_size(dir["directories"][name])
    dir["size"] = size
    return size

def get_deletion_candidates(dir, min_size):
    candidates = []
    if dir["size"] >= min_size:
        candidates.append(dir["size"])
    if "directories" in dir:
        for name in dir["directories"]:
            candidates.extend(get_deletion_candidates(dir["directories"][name], min_size))
    return candidates

def solutionPart2(input):
    required_size = 30000000
    unused_space = 21618835
    min_size = required_size - unused_space

    directories = build_dir_map(input)
    calcualte_size(directories)
    print(directories)
    candidates = get_deletion_candidates(directories, min_size)
    candidates.sort()
    print(f"deletion candidates: {candidates}")
    print(f"size of dir to delete: {min(candidates)}")

if __name__ == "__main__":
    part = int(sys.argv[1])
    inputfile = sys.argv[2]

    print("Solution {} for file {}".format(part, inputfile))

    input = readInput(inputfile)
    if part == 1:
        solutionPart1(input)

    else:
        solutionPart2(input)

