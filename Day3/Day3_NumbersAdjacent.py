sourceFile = open('Day3\input.txt', 'r')
lines = sourceFile.readlines()
lineLength = 140
runningTotal = 0
topLine = ''
midLine = ''
lowLine = ''

def searchForAdjacentChar(number, numIndex):

    if ((topLine != '' and numIndex > 0 and topLine[numIndex-1].isnumeric() == False and topLine[numIndex-1] != '.') or
        (topLine != '' and topLine[numIndex].isnumeric() == False and topLine[numIndex] != '.') or
        (topLine != '' and numIndex < lineLength and topLine[numIndex+1].isnumeric() == False and topLine[numIndex+1] != '.') or
        (numIndex > 0 and midLine[numIndex-1].isnumeric() == False and midLine[numIndex-1] != '.') or
        (numIndex < lineLength and midLine[numIndex+1].isnumeric() == False and midLine[numIndex+1] != '.') or
        (lowLine != '' and numIndex > 0 and lowLine[numIndex-1].isnumeric() == False and lowLine[numIndex-1] != '.') or
        (lowLine != '' and lowLine[numIndex].isnumeric() == False and lowLine[numIndex] != '.') or
        (lowLine != '' and numIndex < lineLength and lowLine[numIndex+1].isnumeric() == False and lowLine[numIndex+1] != '.')):
        
        return True

    return False

# end searchForAdjacentChar

def iterateThroughMidLine():
    global runningTotal
    currentNum = ''
    for midLineIndex in range(len(midLine)):
        if midLine[midLineIndex].isnumeric():
            currentNum += midLine[midLineIndex]
            continue

        if currentNum != '':
            for charNumber in range(len(currentNum)):
                if searchForAdjacentChar(currentNum, midLineIndex-(charNumber+1)):
                    runningTotal += int(currentNum)
                    break
        
        currentNum = ''

for line in lines:
    topLine = midLine
    midLine = lowLine
    lowLine = line.rstrip()

    iterateThroughMidLine()
    

# Finally, search the final line
topLine = midLine
midLine = lowLine
lowLine = ''
iterateThroughMidLine()

print(runningTotal)
        






