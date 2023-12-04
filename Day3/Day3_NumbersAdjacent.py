sourceFile = open('Day3\input.txt', 'r')
lines = sourceFile.readlines()
runningTotal = 0
lineLength = 140

def findAdjacentChars(currentNum, charIdx):

    for char in currentNum:
        # Check 3 spots above
        if charIdx - (lineLength+1) > 0 and (singleFileLine[charIdx-(lineLength+1)].isnumeric() == False and 
                                  singleFileLine[charIdx-(lineLength+1)] != '.'):
            return True
        if charIdx - lineLength > 0 and (singleFileLine[charIdx-lineLength].isnumeric() == False and 
                                  singleFileLine[charIdx-lineLength] != '.'):
            return True
        if charIdx - (lineLength-1) > 0 and (singleFileLine[charIdx-(lineLength-1)].isnumeric() == False and 
                                  singleFileLine[charIdx-(lineLength-1)] != '.'):
            return True
        
        # Check the left & right
        if charIdx - 1 > 0 and (singleFileLine[charIdx-1].isnumeric() == False and 
                                  singleFileLine[charIdx-1] != '.'):
            return True
        if charIdx + 1 < len(singleFileLine) and (singleFileLine[charIdx+1].isnumeric() == False and 
                                                  singleFileLine[charIdx+1] != '.'):
            return True
        
        # Check 3 spots below
        if charIdx + (lineLength-1) < len(singleFileLine) and (singleFileLine[charIdx+(lineLength-1)].isnumeric() == False and 
                                                  singleFileLine[charIdx+(lineLength-1)] != '.'):
            return True
        if charIdx + lineLength < len(singleFileLine) and (singleFileLine[charIdx+lineLength].isnumeric() == False and 
                                                  singleFileLine[charIdx+lineLength] != '.'):
            return True
        if charIdx + (lineLength+1) < len(singleFileLine) and (singleFileLine[charIdx+(lineLength+1)].isnumeric() == False and 
                                                  singleFileLine[charIdx+(lineLength+1)] != '.'):
            return True
        
        # Move on to next char index
        charIdx += 1

    return False


# Set up entire file as one line
singleFileLine = ''
for line in lines:
    singleFileLine += line.rstrip()

currentNum = ''
for charIdx in range(len(singleFileLine)):
    if singleFileLine[charIdx].isnumeric():
        currentNum += singleFileLine[charIdx]
        continue
    elif len(currentNum) > 0:
        if findAdjacentChars(currentNum, charIdx-len(currentNum)):
            runningTotal += int(currentNum)
        currentNum = ''


print(runningTotal)


