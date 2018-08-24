from parseCelebrities import getCupSizes
from trainingSets import popularityImproved
from trainingSets import getTrainingSets
from trainingSets import printTopData
from trainingSets import printData

def getCupIndex(cup):
    cupSizes = getCupSizes()
    return cupSizes.index(cup.lower()) + 1

cupData = open("TrainingSets/Cup/trainingCup.txt", "w+")
cupDataTop = open("TrainingSets/Cup/trainingCupTop.txt", "w+")

for trainingSet in getTrainingSets():
    cupsize, bust, waist, hip, fans = trainingSet
    if cupsize != "" :
        printData(cupData, cupsize, popularityImproved(1,fans))
        printTopData(cupDataTop, cupsize, popularityImproved(1,fans))
