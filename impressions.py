def openReadFile(feature):
    file = open("TrainingSets/" + feature +"/training" + feature + ".txt", "r")
    return file

def openWrtieFile(feature):
    file = open("TrainingSets/" + feature +"/impressions" + feature + ".txt", "w+")
    return file

def getGeneralizedCups(cup):
    if cup >= 1 and cup <= 2:
        return [1,2]
    elif cup >= 5 and cup <= 7:
        return [5,6,7]
    elif cup >= 8 and cup <= 10:
        return [8,9,10]
    elif cup >= 11 and cup <= 13:
        return [11,12,13]
    elif cup >= 14 and cup <= 16:
        return [14,15,16]
    elif cup >= 17 and cup <= 18:
        return [17,18]
    else:
        return [cup]

def getImpressions(feature):
    impressions = {}
    for i in range(0,100) :
        impressions[i] = 0.0
    lines = openReadFile(feature).readlines()
    for line in lines:
        size, fans  = line.strip().split(',')
        if int(size) <= 100:
            if feature != "Ethnicity" and feature != "Cup":
                impressions[int(size)] += float(fans)
                impressions[int(size)-1] += float(fans) / 2.0
                impressions[int(size)+1] += float(fans) / 2.0
            elif feature == "Ethnicity":
                impressions[int(size)] += float(fans)
            elif feature == "Cup":
                for cup in getGeneralizedCups(int(size)):
                    impressions[cup] += float(fans)
    return impressions

def loadImpressions():
    allImpressions = {}
    for feature in ["Bust", "Cup", "Hip", "Waist", "Ethnicity"]:
        impressionsFile = openWrtieFile(feature)
        impressions = getImpressions(feature)
        allImpressions[feature] = impressions
        maxValue = max(impressions.values()) / 100
        for size, fans in reversed(sorted(impressions.iteritems(), key=lambda (k,v): (v,k))):
            impressionsFile.write(str(size) + " " + str(fans / maxValue) + "\n")
            allImpressions[feature][size] /= maxValue
    return allImpressions

