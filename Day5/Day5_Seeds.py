_sourceFile = open('Day5\input.txt', 'r')
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

# Load Seeds
lineIndex = 0
seeds = list(filter(None, _lines[lineIndex].split(':')[1].split(' ')))
for idx in range(len(seeds)):
    seeds[idx] = seeds[idx].rstrip()

# Define generic map traversal
def TraverseMap(sourceArray, mapArray):
    destinationArray = []
    for seed in sourceArray:
        isMapped = False
        for map in mapArray:
            if int(seed) >= int(map[1]) and int(seed) < int(map[1]) + int(map[2]):
                destinationArray.append(int(map[0]) + (int(seed) - int(map[1])))
                isMapped = True
                break
        if(isMapped == False):
            destinationArray.append(seed)
    return destinationArray

# Travers all the maps
soils = TraverseMap(seeds, seedToSoilMap)
fertilizers = TraverseMap(soils, soilToFertilizerMap)
waters = TraverseMap(fertilizers, fertilizerToWaterMap)
lights = TraverseMap(waters, waterToLightMap)
temps = TraverseMap(lights, lightToTempMap)
humids = TraverseMap(temps, tempToHumidityMap)
locations = TraverseMap(humids, humidityToLocationMap)

print(min(locations))