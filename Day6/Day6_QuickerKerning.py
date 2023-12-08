_sourceFile = open('Day6\\input.txt', 'r')
_lines = _sourceFile.readlines()

raceTimes = list(filter(None, _lines[0].rsplit()))[1:]
recordDistances = list(filter(None, _lines[1].rsplit(' ')))[1:]

concatRaceTime = ''
concatRecordDist = ''
for race in raceTimes:
    concatRaceTime += race
for dist in recordDistances:
    concatRecordDist += dist

# Other way takes about a minute...
def RecursiveCheck(priorTime, currentTime, inc, searchType):
    inc *= 2
    distance = currentTime * (int(concatRaceTime) - currentTime)
    if(abs(currentTime - priorTime) == 1):
        return currentTime
    if (distance > int(concatRecordDist) and searchType == "Small") or (distance <= int(concatRecordDist) and searchType == "Big"):
        return RecursiveCheck(int(currentTime), int(int(currentTime) - int(concatRaceTime)/inc), inc, searchType)
    else:
        return RecursiveCheck(int(currentTime), int(int(currentTime) + int(concatRaceTime)/inc), inc, searchType) 

smallestWin = RecursiveCheck(int(concatRaceTime)/2,int(concatRaceTime)/2, 2, "Small")
biggestWin = RecursiveCheck(int(concatRaceTime)/2,int(concatRaceTime)/2, 2, "Big")

print(biggestWin - smallestWin)