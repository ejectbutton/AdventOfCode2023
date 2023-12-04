redCubes = 12
greenCubes = 13
blueCubes = 14

sourceFile = open('Day2\Day2_Input.txt', 'r')
lines = sourceFile.readlines()
runningTotal = 0

for game in lines:
    gameNumber = game.split(':')[0].split(' ')[1]
    allSamples = game.split(':')[1]
    hands = allSamples.split(';')

    isGamePossible = True

    for hand in hands:
        cubes = hand.split(',')
        for cube in cubes:
            if 'green' in cube:
                if int(cube.lstrip().split(' ')[0]) > greenCubes:
                    isGamePossible = False
            if 'red' in cube:
                if int(cube.lstrip().split(' ')[0]) > redCubes:
                    isGamePossible = False
            if 'blue' in cube:
                if int(cube.lstrip().split(' ')[0]) > blueCubes:
                    isGamePossible = False

    if isGamePossible:
        runningTotal += int(gameNumber)

print(runningTotal)
