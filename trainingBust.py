from parseCelebrities import getCupSizes
from trainingSets import popularityImproved
from trainingSets import getTrainingSets
from trainingSets import printTopData
from trainingSets import printData

bustData = open("TrainingSets/Bust/trainingBust.txt", "w+")
bustDataTop = open("TrainingSets/Bust/trainingBustTop.txt", "w+")

for trainingSet in getTrainingSets():
    cupsize, bust, waist, hip, fans = trainingSet
    if bust != "" :
        printData(bustData, bust, popularityImproved(1,fans))
        printTopData(bustDataTop, bust, popularityImproved(1,fans))
