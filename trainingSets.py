from parseCelebrities import getCupSizes

def readDictFromFile(filename):
    file = open(filename, "r")
    lines = file.readlines()
    dictData = {}
    for line in lines:
        key, value = line.split(' ')
        dictData.update({key : value.strip()})
    return dictData

def getMeasurmentValues(cupSizes, measurment):
    bustAndCup, waist, hip = measurment.split('-')
    bust = ''.join(c for c in bustAndCup if not c.isalpha())
    cupStr = ''.join(c for c in bustAndCup if c.isalpha())
    cup = str(cupSizes.index(cupStr.lower())+1)
    return cup, bust, waist, hip

def popularityImproved(groupRate, fans):
    max = 3500.0 / groupRate
    sizingRate = max / 100
    groupedData = int(int(fans)/groupRate)
    sizedData = groupedData/ sizingRate
    return sizedData

def printData(file, data, fans):
    file.write(data + ',' + str(fans) + "\n")

def printTopData(file, data, fans):
    if fans > 5: # arround top 200
        file.write(data + ',' + str(fans) + "\n")

def getTrainingSets():
    measurements, popularity = {}, {}
    measurements = readDictFromFile("celebs-measurements.txt")
    popularity = readDictFromFile("celebs-popularity.txt")
    cupSizes = getCupSizes()
    trainingData = []
    for name, measure in measurements.iteritems():
        if measure.count('-') == 2:
            if name in popularity.keys():
                fans = popularity[name]
                cup, bust, waist, hip = getMeasurmentValues(cupSizes, measure)
                trainingData.append((cup, bust, waist, hip, fans))
    return trainingData
