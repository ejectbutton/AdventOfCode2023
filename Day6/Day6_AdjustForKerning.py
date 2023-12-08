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

waysToBeatRecord = 0
for timeBtnHeld in range(int(concatRaceTime)):
    distance = timeBtnHeld * (int(concatRaceTime) - timeBtnHeld)
    if distance > int(concatRecordDist):
        waysToBeatRecord += 1

print(waysToBeatRecord)