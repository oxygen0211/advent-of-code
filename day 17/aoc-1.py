import copy
input = [
'.#.',
'..#',
'###'
]

currentState = [[
['.','.','.'],
['.','.','.'],
['.','.','.']
],
[
['.','.','.'],
['.','.','.'],
['.','.','.']
],
[
['.','.','.'],
['.','.','.'],
['.','.','.']
]]

for y, row in enumerate(input):
    for x, cube in enumerate(list(row)):
        currentState[1][y][x] = cube

for cycle in range(6):
    nextState = copy.deepcopy(currentState)
    print('Cycle {}'.format(cycle))
    print(currentState)
    for z, plane in enumerate(currentState):
        for y, rows in enumerate(plane):
          for x, cube in enumerate(rows):
              zIndexes = [z]
              if z > 0:
                  zIndexes.append(z - 1)
              if z < len(currentState) - 1:
                  zIndexes.append(z + 1)
              xIndexes = [x]
              if x > 0:
                  xIndexes.append(x - 1)
              if x < len(rows) - 1:
                  xIndexes.append(x + 1)

              yIndexes = [y]
              if y > 0:
                  yIndexes.append(y - 1)
              if y < len(currentState[z]) - 1:
                  yIndexes.append(z + 1)

              activeNeighbors = 0

              for xNeighbor in xIndexes:
                  for yNeighbor in yIndexes:
                      for zNeighbor in zIndexes:

                          if x == xNeighbor and y == yNeighbor and z == zNeighbor:
                              continue

                          print('{}, {}, {}'.format(zNeighbor][yNeighbor][xNeighbor))
                          if currentState[zNeighbor][yNeighbor][xNeighbor] == '#':
                              activeNeighbors += 1

              print('Cube: {}. Active neighbors: {}'.format(cube, activeNeighbors))
              if cube == '#' and (activeNeighbors != 2 or activeNeighbors != 3):
                  nextState[z][y][x] = '.'

              if cube == '.' and activeNeighbors == 3:
                  nextState[z][y][x] = '#'

    currentState = nextState

activeCubes = 0
for plane in currentState:
    for row in plane:
        for cube in row:
            if cube == '#':
                activeCubes += 1

print('Active cubes: {}'.format(activeCubes))
