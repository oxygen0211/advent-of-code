import operator
numberList = [14,1,17,0,3,20]

for i in range(len(numberList), 2020):
    lastNum = numberList[i-1]
    nextNum = 0

    if lastNum in numberList[:i-1]:
        shortenedList = numberList[:i-1]
        lastIndex = len(shortenedList) - operator.indexOf(reversed(shortenedList), lastNum) - 1
        nextNum = (i-1) - lastIndex

    numberList.append(nextNum)

print(numberList[len(numberList)-1])
