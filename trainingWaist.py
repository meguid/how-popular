from parseCelebrities import getCupSizes
from trainingSets import popularityImproved
from trainingSets import getTrainingSets
from trainingSets import printTopData
from trainingSets import printData

waistData = open("TrainingSets/Waist/trainingWaist.txt", "w+")
waistDataTop = open("TrainingSets/Waist/trainingWaistTop.txt", "w+")

for trainingSet in getTrainingSets():
    cupsize, bust, waist, hip, fans = trainingSet
    if waist != "" :
        printData(waistData, waist, popularityImproved(1,fans))
        printTopData(waistDataTop, waist, popularityImproved(1,fans))
