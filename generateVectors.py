def readDictFromFile(filename):
    file = open(filename, "r")
    lines = file.readlines()
    dictData = {}
    for line in lines:
        key, value = line.split(' ')
        dictData.update({key : value.strip()})
    return dictData

def getMeasurmentValues(measurment):
    bustAndCup, waist, hip = measurment.split('-')
    bust = ''.join(c for c in bustAndCup if not c.isalpha())
    cup = ''.join(c for c in bustAndCup if c.isalpha())
    return cup, bust, waist, hip

def generateVectors():
    measurements, popularity = {}, {}
    measurements = readDictFromFile("celebs-measurements.txt")
    popularity = readDictFromFile("celebs-popularity.txt")
    cupVectorFile = open("vector-cup.txt", "w")
    bustVectorFile = open("vector-bust.txt", "w")
    waistVectorFile = open("vector-waist.txt", "w")
    hipVectorFile = open("vector-hip.txt", "w")
    measurementVectorFile = open("vector-measurement.txt", "w")
    for name, measure in measurements.iteritems():
        if measure.count('-') == 2:
            if name in popularity.keys():
                fans = popularity[name]
                cup, bust, waist, hip = getMeasurmentValues(measure)
                cupVectorFile.write(cup + ',' + fans + "\n")
                bustVectorFile.write(bust + ',' + fans + "\n")
                waistVectorFile.write(waist + ',' + fans + "\n")
                hipVectorFile.write(hip + ',' + fans + "\n")
                measurementVectorFile.write(cup + ',' + bust + ',' + waist + ',' + hip + ',' + fans + "\n")

generateVectors()
