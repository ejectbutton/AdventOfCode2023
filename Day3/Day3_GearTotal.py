# Globals
sourceFile = open('Day3\input.txt', 'r')
lines = sourceFile.readlines()
lineLength = 140
runningTotal = 0
topLine = ''
midLine = ''
lowLine = ''

def IterateThroughMidLine():
    global runningTotal
    for midLineIndex in range(len(midLine)):
        if midLine[midLineIndex] == '*':
            listAdjacent = SearchForAdjacentNumbers(midLineIndex)
            seen = []
            for number in listAdjacent:
                if number in seen:
                    print("Number repeated!")
                else:
                    seen.append(number)
            if len(listAdjacent) == 2:
                runningTotal += int(listAdjacent[0]) * int(listAdjacent[1])
# end iterateThroughMidLine

def SearchForAdjacentNumbers(midLineIndex):

    adjacentNumbers = []
    if (topLine != ''):
        priorNumber = ''
        # TopLeft
        if(midLineIndex > 0 and topLine[midLineIndex-1].isnumeric()):
            topLeftNumber = FindContainingNumber(topLine, midLineIndex-1)
            adjacentNumbers.append(topLeftNumber)
            priorNumber = topLeftNumber

        # TopMid
        if(topLine[midLineIndex] == '.'):
            priorNumber = ''
        elif(topLine[midLineIndex].isnumeric() and priorNumber == ''):
            topMidNumber = FindContainingNumber(topLine, midLineIndex)
            adjacentNumbers.append(topMidNumber)
            priorNumber = topMidNumber
        
        # TopRight
        if(midLineIndex < lineLength and topLine[midLineIndex+1].isnumeric() and priorNumber == ''):
            topRightNumber = FindContainingNumber(topLine, midLineIndex+1)
            adjacentNumbers.append(topRightNumber)
    
    # Left
    if(midLineIndex > 0 and midLine[midLineIndex-1].isnumeric()):
        leftNumber = FindContainingNumber(midLine, midLineIndex-1)
        adjacentNumbers.append(leftNumber)

    # Right
    if(midLineIndex < lineLength and midLine[midLineIndex+1].isnumeric()):
        rightNumber = FindContainingNumber(midLine, midLineIndex+1)
        adjacentNumbers.append(rightNumber)
    
    if (lowLine != ''):
        priorNumber = ''
        # LowLeft
        if(midLineIndex > 0 and lowLine[midLineIndex-1].isnumeric()):
            lowLeftNumber = FindContainingNumber(lowLine, midLineIndex-1)
            adjacentNumbers.append(lowLeftNumber)
            priorNumber = lowLeftNumber
        
        # LowMid
        if(lowLine[midLineIndex] == '.'):
            priorNumber = ''
        elif(lowLine[midLineIndex].isnumeric() and priorNumber == ''):
            lowMidNumber = FindContainingNumber(lowLine, midLineIndex)
            adjacentNumbers.append(lowMidNumber)
            priorNumber = lowMidNumber

        # LowRight
        if(midLineIndex < lineLength and lowLine[midLineIndex+1].isnumeric() and priorNumber == ''):
            lowRightNumber = FindContainingNumber(lowLine, midLineIndex+1)
            adjacentNumbers.append(lowRightNumber)

    return adjacentNumbers
# end SearchForAdjacentNumbers

def FindContainingNumber(line, index):
    thisNumber = line[index]
    inc = 1
    while(line[index-inc].isnumeric()):
        thisNumber = line[index-inc] + thisNumber
        inc += 1
    
    inc = 1
    while(line[index+inc].isnumeric()):
        thisNumber += line[index+inc]
        inc += 1
    
    return thisNumber
#end FindContainingNumbers


for line in lines:
    topLine = midLine
    midLine = lowLine
    lowLine = line.rstrip()

    IterateThroughMidLine()
    
print(runningTotal)
        





