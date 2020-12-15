import operator
numberList = [14,1,17,0,3,20]

numberIndexes = {}
lastNum = 0

for i, num in enumerate(numberList):
    lastNum = num
    numberIndexes[num] = i

# Problem: after ~ i = 100.000 performance drops, probably due to RAM.
# Idea: replace searching indexof searchin in list with storing last index in a dict
#for i in range(30000000):
for i in range(len(numberList), 30000000):
    nextNum = 0

    if lastNum in numberIndexes.keys():
        lastIndex = numberIndexes[lastNum]
        nextNum = (i-1) - lastIndex

    numberIndexes[lastNum] = i-1
    lastNum = nextNum

    if i % 500000 == 0:
        print('i: {}, setting lastNum = {}'.format(i, lastNum))
print(lastNum)
