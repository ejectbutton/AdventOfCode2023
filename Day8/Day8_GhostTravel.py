from functools import reduce

SOURCEFILE = open('Day8\\input.txt', 'r')
LINES = SOURCEFILE.readlines()

directions = LINES[0].rstrip()
leftTurns = {}
rightTurns = {}
for map in LINES[2:]:
    location = map.split('=')[0].rstrip()
    leftTurns.update({location: map.split('(')[1].split(',')[0]})
    rightTurns.update({location: map.split(',')[1].split(')')[0].lstrip()})

allPathLengths = []
for currentLocation in leftTurns.keys():
    if currentLocation[2] != 'A': 
        continue
    
    directionIndex = 0
    turnsTaken = 0
    while(currentLocation[2] != 'Z'):
        if directions[directionIndex] == 'L':
            currentLocation = leftTurns[currentLocation]
        else:
            currentLocation = rightTurns[currentLocation]
        turnsTaken += 1
        directionIndex += 1
        if directionIndex == len(directions):
            directionIndex = 0
    allPathLengths.append(turnsTaken)

print(allPathLengths)
# Alright, now we know how long it takes for each of these to finish. Now we ask, do they share any factors?
def FindFactors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
# end factors

def EnumerateFactors(listOfNumbers):
    retList = []
    for path in listOfNumbers:
        facs = FindFactors(int(path))
        facs.remove(1)
        facs.remove(path)
        retList.append(sorted(facs))
    return retList
# end populateFactors

def FindCommonFactor(allFactors):
    for item in allFactors[0]:
        foundCommonality = True
        for factrList in allFactors[1:]:
            thisFactorCommon = False
            for factor in factrList:
                if item == factor: 
                    thisFactorCommon = True
            if thisFactorCommon == False:
                foundCommonality = False
                break
        if foundCommonality: return int(item)
    return -1
# end FindCommonFactor

def IsPrimeNumber(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0: break
        else: return True
    else: return False
# end IsPrimeNumber

fList = EnumerateFactors(allPathLengths)
newFactors = []
cf = FindCommonFactor(fList)
if cf != -1:
    for item in fList:
        item.remove(cf)
        newFactors.append(item[0])

allArePrime = True
for factor in newFactors:
    if IsPrimeNumber(factor) == False:
        allArePrime = False

if allArePrime:
    total = cf
    for num in newFactors: total *= int(num)
    print(total)

