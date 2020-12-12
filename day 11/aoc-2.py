from simplejson import dumps
input = [
'#.##.##.##',
'#######.##',
'#.#.#..#..',
'####.##.##',
'#.##.##.##',
'#.#####.##',
'..#.#.....',
'##########',
'#.######.#',
'#.#####.##'
]

def aboveIsOccupied(i, j, currentSeatplan):
    # above
    if i > 0:
        if currentSeatplan[i-1][j] == '#':
            return True

        if currentSeatplan[i-1][j] == '.':
            return aboveIsOccupied(i-1, j, currentSeatplan)

    return False

def belowIsOccupied(i, j, currentSeatplan):
    # above
    if i < len(currentSeatplan) - 1:
        if currentSeatplan[i+1][j] == '#':
            return True

        if currentSeatplan[i+1][j] == '.':
            return belowIsOccupied(i+1, j, currentSeatplan)

    return False

def leftIsOccupied(i, j, currentSeatplan):
    # above
    if j > 0:
        if currentSeatplan[i][j-1] == '#':
            return True

        if currentSeatplan[i][j-1] == '.':
            return leftIsOccupied(i, j-1, currentSeatplan)

    return False

def rightIsOccupied(i, j, currentSeatplan):
    # above
    if j < len(currentSeatplan[i]) - 1:
        if currentSeatplan[i][j+1] == '#':
            return True

        if currentSeatplan[i][j+1] == '.':
            return rightIsOccupied(i, j+1, currentSeatplan)

    return False

def upperLeftIsOccupied(i, j, currentSeatplan):
    # above
    if i > 0 and j > 0:
        if currentSeatplan[i-1][j-1] == '#':
            return True

        if currentSeatplan[i-1][j-1] == '.':
            return upperLeftIsOccupied(i-1, j-1, currentSeatplan)

    return False

def upperRightIsOccupied(i, j, currentSeatplan):
    # above
    if i > 0 and j < len(currentSeatplan[i]) - 1:
        if currentSeatplan[i-1][j+1] == '#':
            return True

        if currentSeatplan[i-1][j+1] == '.':
            return upperLeftIsOccupied(i-1, j+1, currentSeatplan)

    return False

def bottomLeftIsOccupied(i, j, currentSeatplan):
    # above
    if i < len(currentSeatplan) - 1 and j > 0:
        if currentSeatplan[i+1][j-1] == '#':
            return True

        if currentSeatplan[i+1][j-1] == '.':
            return bottomLeftIsOccupied(i+1, j-1, currentSeatplan)

    return False

def bottomRightIsOccupied(i, j, currentSeatplan):
    # above
    if i < len(currentSeatplan) - 1 and j < len(currentSeatplan[i]) - 1:
        if currentSeatplan[i+1][j+1] == '#':
            return True

        if currentSeatplan[i+1][j+1] == '.':
            return bottomRightIsOccupied(i+1, j+1, currentSeatplan)

    return False

def getAdjacentOccupiedSpaces(i, j, currentSeatplan):
    occupied = 0
    # above
    if aboveIsOccupied(i, j, currentSeatplan):
        occupied += 1

    # below
    if belowIsOccupied(i, j, currentSeatplan):
        occupied += 1

    # left
    if leftIsOccupied(i, j, currentSeatplan):
        occupied += 1

    # right
    if rightIsOccupied(i, j, currentSeatplan):
        occupied += 1

    # upper-left
    if upperLeftIsOccupied(i, j, currentSeatplan):
        occupied += 1

    # upper-right
    if upperRightIsOccupied(i, j, currentSeatplan):
        occupied += 1

    # bottom-left
    if bottomLeftIsOccupied(i, j, currentSeatplan):
        occupied += 1

    # bottom-right
    if bottomRightIsOccupied(i, j, currentSeatplan):
        occupied += 1

    return occupied

def shouldBecomeOccupied(i, j, currentSeatplan):
    return getAdjacentOccupiedSpaces(i, j, currentSeatplan) < 1

def shouldBecomeFree(i, j, currentSeatplan):
    return getAdjacentOccupiedSpaces(i, j, currentSeatplan) >= 5

def updateSeatPlan(currentSeatplan):
    newSeatPlan = []
    for i, row in enumerate(currentSeatplan):
        newRow = []
        for j, state in enumerate(row):
            newState = state

            if state == 'L'and shouldBecomeOccupied(i, j, currentSeatplan):
                newState = '#'

            if state == '#' and shouldBecomeFree(i, j, currentSeatplan):
                newState = 'L'

            newRow.append(newState)

        newSeatPlan.append(newRow)

    return newSeatPlan

currentSeatplan = input
stabilityReached = False
while not stabilityReached:
    occupiedSeats = 0
    newSeatplan = updateSeatPlan(currentSeatplan)
    stabilityReached = dumps(currentSeatplan) == dumps(newSeatplan)
    print('Status stable? {}'.format(stabilityReached))
    currentSeatplan = newSeatplan

    for row in currentSeatplan:
        rowString = ''
        for seat in row:
            rowString += seat
            if seat == '#':
                occupiedSeats += 1

        print(rowString)

print('Occupied: {}'.format(occupiedSeats))
