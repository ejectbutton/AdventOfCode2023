
allNumbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def scanNumber(inputString):
    eliminatedNumbers = []
    currentIndex = 0


    while (len(eliminatedNumbers) != 10):
        for num in allNumbers:
            if num in eliminatedNumbers:
                continue
            elif inputString[currentIndex] != num[currentIndex]:
                eliminatedNumbers.append(num)
            elif currentIndex == len(num) - 1:
                return allNumbers.index(num)
        currentIndex += 1

    return -1
    


sourceFile = open('Day1\Day1_Input.txt', 'r')
lines = sourceFile.readlines()
runningTotal = 0

for line in lines:
    partOfNumberIndex = 0
    start = -1
    end = -1

    for charIndex in range(len(line)):
        if line[charIndex].isnumeric():
            partOfNumberIndex = 0
            if (start == -1): 
                start = int(line[charIndex])
            end = int(line[charIndex])

        else:
            numberAtIdx = scanNumber(line[charIndex:])
            if(numberAtIdx >= 0):
                partOfNumberIndex = 0
                if (start == -1): 
                    start = int(numberAtIdx)
                end = int(numberAtIdx)
    
    print(start*10 + end)
    runningTotal += start*10 + end

print(runningTotal)







