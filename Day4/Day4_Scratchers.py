_sourceFile = open('Day4\input.txt', 'r')
_lines = _sourceFile.readlines()
_runningTotal = 0

for scratcher in _lines:
    winningNumbers = list(filter(None, scratcher.split(':')[1].split('|')[0].split(' ')))
    myNumbers = list(filter(None, scratcher.split(':')[1].split('|')[1].split(' ')))

    scratcherValue = 0
    winnersFound = 0
    for number in myNumbers:
        if number.rstrip() in winningNumbers:
            scratcherValue = pow(2,winnersFound)
            winnersFound += 1
    
    _runningTotal += scratcherValue

print(_runningTotal)