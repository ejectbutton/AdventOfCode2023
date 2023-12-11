SOURCEFILE = open('Day8\\input.txt', 'r')
LINES = SOURCEFILE.readlines()

directions = LINES[0].rstrip()
leftTurns = {}
rightTurns = {}
for map in LINES[2:]:
    location = map.split('=')[0].rstrip()
    leftTurns.update({location: map.split('(')[1].split(',')[0]})
    rightTurns.update({location: map.split(',')[1].split(')')[0].lstrip()})

currentLocation = 'AAA'
directionIndex = 0
turnsTaken = 0

while(currentLocation != 'ZZZ'):
    if directions[directionIndex] == 'L':
        currentLocation = leftTurns[currentLocation]
    else:
        currentLocation = rightTurns[currentLocation]
    turnsTaken += 1
    directionIndex += 1
    if directionIndex == len(directions):
        directionIndex = 0

print(turnsTaken)