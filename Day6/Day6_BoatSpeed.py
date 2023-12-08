_sourceFile = open('Day6\\input.txt', 'r')
_lines = _sourceFile.readlines()

raceTimes = list(filter(None, _lines[0].rsplit()))[1:]
recordDistances = list(filter(None, _lines[1].rsplit(' ')))[1:]

marginOfError = 1
for gameIndex in range(len(raceTimes)):
    waysToBeatRecord = 0
    for timeBtnHeld in range(int(raceTimes[gameIndex])):
        distance = timeBtnHeld * (int(raceTimes[gameIndex]) - timeBtnHeld)
        if distance > int(recordDistances[gameIndex]):
            waysToBeatRecord += 1
    marginOfError *= waysToBeatRecord

print(marginOfError)