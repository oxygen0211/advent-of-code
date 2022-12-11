from os import error
import sys

element_scores = {
    # Rock
    'X': 1,
    # Paper
    'Y': 2,
    # Scissors
    'Z': 3
}

win_combinations = {
    # Rock
    'A': 'Y',
    # Paper
    'B': 'Z',
    # Scissors
    'C': 'X'
}

draw_combinations = {
    # Rock
    'A': 'X',
    # Paper
    'B': 'Y',
    # Scissors
    'C': 'Z'
}

loss_combinations = {
    # Rock
    'A': 'Z',
    # Paper
    'B': 'X',
    # Scissors
    'C': 'Y'
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
                input.append(line.strip().split())

    return input

def solutionPart1(input):
    print(input)
    total_score = 0

    for round in input:
        score = 0
        opponent = round[0]
        own = round[1]

        print(f"shooting {own} agains {opponent}")
        score += element_scores[own]

        if win_combinations[opponent] == own:
            print("Won!")
            score += 6
        
        elif draw_combinations[opponent] == own:
            print("Draw!")
            score += 3

        else:
            print("Lost!")

        total_score += score

    print(f"Game scored a total of {total_score}")


def solutionPart2(input):
    print(input)
    total_score = 0

    for round in input:
        score = 0
        opponent = round[0]
        instruction = round[1]

        if 'Z' == instruction:
            print("Need to win!")
            own = win_combinations[opponent]
            score += 6
        
        elif 'Y' == instruction:
            print("Need to throw a draw!")
            own = draw_combinations[opponent]
            score += 3

        else:
            print("Need to loose!")
            own = loss_combinations[opponent]
        
        print(f"shooting {own} for a score of {element_scores[own]}")
        score += element_scores[own]
        total_score += score

    print(f"Game scored a total of {total_score}")

if __name__ == "__main__":
    part = int(sys.argv[1])
    inputfile = sys.argv[2]

    print("Solution {} for file {}".format(part, inputfile))

    input = readInput(inputfile)
    if part == 1:
        solutionPart1(input)

    else:
        solutionPart2(input)

