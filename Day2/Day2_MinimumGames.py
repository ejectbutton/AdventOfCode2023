sourceFile = open('Day2\Day2_Input.txt', 'r')
lines = sourceFile.readlines()
runningTotal = 0

for game in lines:
    minRedCubes = 0
    minGreenCubes = 0
    minBlueCubes = 0

    gameNumber = game.split(':')[0].split(' ')[1]
    allSamples = game.split(':')[1]
    hands = allSamples.split(';')

    for hand in hands:
        cubes = hand.split(',')
        for cube in cubes:
            if 'green' in cube:
                if int(cube.lstrip().split(' ')[0]) > minGreenCubes:
                    minGreenCubes = int(cube.lstrip().split(' ')[0])
            if 'red' in cube:
                if int(cube.lstrip().split(' ')[0]) > minRedCubes:
                    minRedCubes = int(cube.lstrip().split(' ')[0])
            if 'blue' in cube:
                if int(cube.lstrip().split(' ')[0]) > minBlueCubes:
                    minBlueCubes = int(cube.lstrip().split(' ')[0])

    runningTotal += minRedCubes * minGreenCubes * minBlueCubes

print(runningTotal)
