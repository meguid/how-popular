from celebs import getCupSizes

cupSizes = getCupSizes()
ethnicities = ['Asian', 'Asian/Indian', 'Black', 'Middle Eastern', 'Multiracial', 'White', 'OTHER']
celebsBiographyFile = open("celebs-biography.txt", "r")
celebsFeaturesFile = open("celebs-features.txt", "w+")
celebsPopularityFile = open("celebs-popularity.txt", "r")

def getMeasurmentValues(measurment):
    cup, bust, waist, hip = "","","",""
    if measurments != "":
        bustAndCup, waist, hip = measurment.split('-')
        bust = ''.join(c for c in bustAndCup if not c.isalpha())
        cupStr = ''.join(c for c in bustAndCup if c.isalpha())
        cup = str(cupSizes.index(cupStr.lower())+1)
        feature = cup, bust, waist, hip
        return feature
    else:
        feature = cup, bust, waist, hip
        return (cup, bust, waist, hip)

def getPopularity(name):
    if name in popularity.keys():
        return popularity[name]
    else:
        return "0"

lines = celebsBiographyFile.readlines()
name = ""
measurments = ""
ethnicity = ""
features = []
for line in lines:
    line = line.strip()
    if line[0:3] == "$$$":
        cup, bust, waist, hip = getMeasurmentValues(measurments)
        features.append((name, cup, bust, waist, hip, ethnicity))
        name = line[4:]
    elif line[0:21] == "Measurements (inches)":
        if '--' not in (line[26:])[:-2] and (line[26:])[:-2].count('-') == 2:
            measurments = (line[26:])[:-2]
    elif line[0:9] == "Ethnicity":
        ethnicity = str(ethnicities.index((line[14:])[:-2])+1)

lines = celebsPopularityFile.readlines()
for line in lines:
    name, fans = line.split(' ')
    fans = fans.strip()
    for fname, cup, bust, waist, hip, ethnicity in features:
        if name == fname:
            celebsFeaturesFile.write(name + " $ " + cup + " $ " + bust + " $ " + waist + " $ " + hip + " $ " + ethnicity + " $ " + fans + "\n")
