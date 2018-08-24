from parseCelebrities import getCupSizes
from trainingSets import popularityImproved
from trainingSets import getTrainingSets
from trainingSets import printTopData
from trainingSets import printData

hipData = open("TrainingSets/Hip/trainingHip.txt", "w+")
hipDataTop = open("TrainingSets/Hip/trainingHipTop.txt", "w+")

for trainingSet in getTrainingSets():
    cupsize, bust, waist, hip, fans = trainingSet
    if hip != "" :
        printData(hipData, hip, popularityImproved(1,fans))
        printTopData(hipDataTop, hip, popularityImproved(1,fans))
