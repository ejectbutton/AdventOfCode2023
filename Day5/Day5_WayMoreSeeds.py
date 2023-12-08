_sourceFile = open('Day5\\input.txt', 'r')
_lines = _sourceFile.readlines()

def ScanForLine(identifier):
    for idx in range(len(_lines)):
        if identifier in _lines[idx]:
            return idx

def loadValues(startIdx, count):
    stringList = []
    returnList = []
    for lineItr in range(count):
        returnList.append(_lines[startIdx+lineItr].replace('\n', '').split(' '))
    return returnList

seedToSoilIdx = ScanForLine('seed-to-soil') + 1
soilToFertIdx = ScanForLine('soil-to-fertilizer') + 1
fertToWaterIdx = ScanForLine('fertilizer-to-wate') + 1
waterToLightIdx = ScanForLine('water-to-light') + 1
lightToTempIdx = ScanForLine('light-to-temperature') + 1
tempToHumidIdx = ScanForLine('temperature-to-humidity') + 1
humidityToLocationIdx = ScanForLine('humidity-to-location') + 1

seedToSoilMap = loadValues(seedToSoilIdx, soilToFertIdx - seedToSoilIdx - 2)
soilToFertilizerMap = loadValues(soilToFertIdx, fertToWaterIdx - soilToFertIdx - 2)
fertilizerToWaterMap = loadValues(fertToWaterIdx, waterToLightIdx - fertToWaterIdx - 2)
waterToLightMap = loadValues(waterToLightIdx, lightToTempIdx - waterToLightIdx - 2)
lightToTempMap = loadValues(lightToTempIdx, tempToHumidIdx - lightToTempIdx - 2)
tempToHumidityMap = loadValues(tempToHumidIdx, humidityToLocationIdx - tempToHumidIdx - 2)
humidityToLocationMap = loadValues(humidityToLocationIdx, len(_lines) - humidityToLocationIdx)

# Define generic map traversal
# There are 6 basic ways a map can apply to a source:
# 1. The map can start before & end within the range ends
# 2. The map can start within & end after the range ends
# 3. The map can start within & end before the range ends
# 4. The map can start before & end within the range ends
# 5. The map can start before & end before the range starts (just ignore it)
# 6. The map can start after & end after the range ends (just ignore it)
def TraverseMap(sourceArray, mapArray):
    destinationArray = []
    for itemPair in sourceArray:
        sourceStart = int(itemPair.split(':')[0])
        sourceRange = int(itemPair.split(':')[1])
        isMapped = False
        for map in mapArray:
            if sourceStart > int(map[1]) + int(map[2]):
                continue
            elif sourceStart + sourceRange < int(map[1]):
                continue
            else:
                if int(map[1]) < sourceStart:
                    destStart = int(map[0]) + sourceStart - int(map[1])
                    destRange = sourceRange
                    if (sourceStart - int(map[1])) + sourceRange < int(map[2]):
                        print("1. This map fully engulfs the entire sourceRange")
                    else:
                        print("2. This map starts before the sourceStart, and ends within it")
                        destRange = int(map[2]) - (sourceStart - int(map[1]))
                    destinationArray.append(str(destStart) + ':' + str(destRange))
                elif int(map[1]) + int(map[2]) >= sourceStart + sourceRange:
                    print("3. This map starts within the sourceRange and ends outside it")
                    destRange = (sourceStart + sourceRange) - int(map[1])
                    destinationArray.append(map[0] + ':' + str(destRange))
                else:
                    print("4. This map starts & ends within the sourceRange")
                    destinationArray.append(map[0] + ':' + map[2])

                isMapped = True

        if isMapped == False:
            print("This source never mapped to anything")
            destinationArray.append(itemPair)

    return destinationArray
# end TraverseMap

# Load Seeds
lineIndex = 0
seedsLine = list(filter(None, _lines[lineIndex].split(':')[1].split(' ')))
seeds = []
for idx in range(int(len(seedsLine)/2)):
    seed = seedsLine[idx*2] + ':' + seedsLine[idx*2+1]
    seeds.append(seed.rstrip())
    
# Travers all the maps
soils = TraverseMap(seeds, seedToSoilMap)
fertilizers = TraverseMap(soils, soilToFertilizerMap)
waters = TraverseMap(fertilizers, fertilizerToWaterMap)
lights = TraverseMap(waters, waterToLightMap)
temps = TraverseMap(lights, lightToTempMap)
humids = TraverseMap(temps, tempToHumidityMap)
locations = TraverseMap(humids, humidityToLocationMap)

lowestLocation = -1
for location in locations:
    locationNum = int(location.split(':')[0])
    lowestLocation = locationNum if locationNum < lowestLocation or lowestLocation == -1 else lowestLocation

print(lowestLocation)