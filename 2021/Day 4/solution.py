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
                input.append(line.strip())
                
    return input

def buildBoardStructure(input):
    numbers = [int(n) for n in input[0].split(',')]

    boards = []
    board = []
    for line in input[2:]:
        if line == '':
            boards.append(board)
            board = []
            continue
        
        col = []
        for char in line.split(' '):
            if char == '':
                continue
            col.append(int(char))
            
        board.append(col)
    
    boards.append(board)

    return(numbers, boards)

def markBoard(number, board):
    for i in range(5):
        for j in range(5):
            if board[i][j] == number:
                board[i][j] = "X"
    return board

def checkHorizontal(board):
    for i in range(5):
        rowMatched = True
        for j in range(5):
            rowMatched = rowMatched and board[i][j] == "X"
        
        if rowMatched:
            return True
    return False

def checkVertical(board):
    for i in range(5):
        rowMatched = True
        for j in range(5):
            rowMatched = rowMatched and board[j][i] == "X"
        
        if rowMatched:
            return True
    return False

def checkBoard(board):
    if checkHorizontal(board):
        return True

    if checkVertical(board):
        return True
    
    return False

def playBoard(numbers, board):
    for i in range(len(numbers)):
        board = markBoard(numbers[i], board)
        if checkBoard(board):
            return (i, board)

    return (-1, board)

def calculateSum(winningBoard):
    boardSum = 0
    for i in range(5):
        for j in range(5):
            if not winningBoard[i][j] == "X":
                boardSum += winningBoard[i][j]
    
    return boardSum

def solutionPart1(input):
    (numbers, boards) = buildBoardStructure(input)
    print("Numbers: {}".format(numbers))
    print("Boards: {}".format(boards))

    winningBoard = []
    winninRound = -1

    for board in boards:
        (endRound, finalBoard) = playBoard(numbers, board)

        if winninRound < 0 or endRound < winninRound:
            winningBoard = board
            winninRound = endRound
    
    print("Winning board after round {}: {}".format(winninRound, winningBoard))

    winningNumber = numbers[winninRound]
    boardSum = calculateSum(winningBoard)

    print("Answer: {} * {} = {}".format(boardSum, winningNumber, boardSum * winningNumber))

def solutionPart2(input):
    (numbers, boards) = buildBoardStructure(input)
    print("Numbers: {}".format(numbers))
    print("Boards: {}".format(boards))

    winningBoard = []
    winninRound = -1

    for board in boards:
        (endRound, finalBoard) = playBoard(numbers, board)

        if endRound > winninRound:
            winningBoard = board
            winninRound = endRound
    
    print("Winning board after round {}: {}".format(winninRound, winningBoard))

    winningNumber = numbers[winninRound]
    boardSum = calculateSum(winningBoard)

    print("Answer: {} * {} = {}".format(boardSum, winningNumber, boardSum * winningNumber))

if __name__ == "__main__":
    part = int(sys.argv[1])
    inputfile = sys.argv[2]

    print("Solution {} for file {}".format(part, inputfile))

    input = readInput(inputfile)
    if part == 1:
        solutionPart1(input)

    else:
        solutionPart2(input)

