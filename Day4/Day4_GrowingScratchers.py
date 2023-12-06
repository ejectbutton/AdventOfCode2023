_sourceFile = open('Day4\input.txt', 'r')
_lines = _sourceFile.readlines()
_runningTotal = 0

ticketCount = []
for i in range(len(_lines)):
    ticketCount.append(1)

for scratcherIdx in range(len(_lines)):
    winningNumbers = list(filter(None, _lines[scratcherIdx].split(':')[1].split('|')[0].split(' ')))
    myNumbers = list(filter(None, _lines[scratcherIdx].split(':')[1].split('|')[1].split(' ')))

    winnersFound = 0
    for number in myNumbers:
        if number.rstrip() in winningNumbers:
            winnersFound += 1
            
    for addlTickets in range(winnersFound):
        ticketCount[scratcherIdx+(addlTickets+1)] += ticketCount[scratcherIdx]
   
print(sum(ticketCount))