from predict import getScore

celebsFeaturesFile = open("celebs-features.txt", "r")
celebsPredectionsFile = open("celebs-prediction.txt", "w+")
celebsPredectionsSortedFile = open("celebs-prediction-sorted.txt", "w+")

cupData = open("TrainingSets/Cup/trainingCup.txt", "w+")
cupDataTop = open("TrainingSets/Cup/trainingCupTop.txt", "w+")

waistData = open("TrainingSets/Waist/trainingWaist.txt", "w+")
waistDataTop = open("TrainingSets/Waist/trainingWaistTop.txt", "w+")

hipData = open("TrainingSets/Hip/trainingHip.txt", "w+")
hipDataTop = open("TrainingSets/Hip/trainingHipTop.txt", "w+")

bustData = open("TrainingSets/Bust/trainingBust.txt", "w+")
bustDataTop = open("TrainingSets/Bust/trainingBustTop.txt", "w+")

ethnicityData = open("TrainingSets/Ethnicity/trainingEthnicity.txt", "w+")
ethnicityDataTop = open("TrainingSets/Ethnicity/trainingEthnicityTop.txt", "w+")

celebsPredictions = {}

def popularityImproved(groupRate, fans):
    max = 3500.0 / groupRate
    sizingRate = max / 100
    groupedData = int(int(fans)/groupRate)
    sizedData = groupedData/ sizingRate
    return sizedData

def printData(file, data, fans):
    file.write(data + ',' + str(fans) + "\n")

def printTopData(file, data, fans):
    if fans > 5: # around top 200
        file.write(data + ',' + str(fans) + "\n")

def printGeneral(file, topFile, data, fans):
    if data != "" :
        printData(file, data, popularityImproved(1,fans))
        printTopData(topFile, data, popularityImproved(1,fans))

def printPrediction(name, cup, bust, waist, hip, fans):
    if bust != "" and cup != "" and waist != "" and hip != "" :
        measurement = str(cup) + " " + str(bust) + " " + str(waist) + " " + str(hip)
        score = getScore(measurement)
        celebsPredectionsFile.write(name + " " + str(score) + "\n")
        celebsPredictions[name] = score

lines = celebsFeaturesFile.readlines()
for line in lines:
    name, cup, bust, waist, hip, ethnicity, fans  = line.strip().split(' $ ')
    printGeneral(cupData, cupDataTop, cup, fans)
    printGeneral(bustData, bustDataTop, bust, fans)
    printGeneral(waistData, waistDataTop, waist, fans)
    printGeneral(hipData, hipDataTop, hip, fans)
    printGeneral(ethnicityData, ethnicityDataTop, ethnicity, fans)
    printPrediction(name, cup, bust, waist, hip, fans)

for name, prediction in reversed(sorted(celebsPredictions.iteritems(), key=lambda (k,v): (v,k))):
    celebsPredectionsSortedFile.write(name + ' ' + str(prediction) + "\n")

