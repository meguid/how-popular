from lxml import html
import requests

from getCelebsCupSizes import getCelebsCupSizes

def getCelebsNames(cupSizes) :
    fullCelebsList = set()
    fullCelebsFile = open("celebs.txt", "w")
    fullCelebsFileNumbered = open("celebs_numbered.txt", "w")
    for cupsize in cupSizes:
        celebsFile = open("Celebrities Names By Cup Size/celebs_" + cupsize + ".txt", "r")
        celebs = celebsFile.readlines()
        for celeb in celebs:
            if celeb not in fullCelebsList:
                fullCelebsList.add(celeb)
    index = 1
    for celeb in sorted(fullCelebsList):
        fullCelebsFile.write(celeb)
        fullCelebsFileNumbered.write(str(index) + ": " + celeb)
        index += 1
    return sorted(list(fullCelebsList))

getCelebsNames(getCelebsCupSizes())

