from impressions import loadImpressions

celebsPredectionsFile = open("celebs-prediction.txt", "r")
celebsPredectionsSortedFile = open("celebs-prediction-sorted.txt", "r")

cupSizes = ['a', 'aa', 'b', 'c', 'd', 'dd', 'ddd', 'e', 'ee', 'eee', 'f', 'ff', 'fff', 'g', 'gg', 'ggg', 'h', 'hh', 'j', 'kk', 'l']
impressions = loadImpressions()

def celebritiesList(celebrities):
    celebs = list(map((lambda celebrity: celebrity.replace("-", " ").title()), celebrities))
    return ', '.join([str(x) for x in celebs[:-2]]) + ", " + ', and '.join([str(x) for x in celebs[-2:]])

def intro(score):
    return ["Ohh", "Heeey!!", "GOOO GIRL", "Awesome!", "INCREDIBLE", "OH MY G!!"][int(score/20)]

def convert(measurements) :
    cup, bust, waist, hip = measurements.split(' ')
    cup = str(cupSizes.index(cup.lower())+1)
    measurements = cup + " " + bust + " " + waist + " " + hip
    return measurements

def score(measurements):
    cup, bust, waist, hip = measurements.split(' ')
    cupImp = impressions["Cup"][min(int(cup),99)]
    bustImp = impressions["Bust"][min(int(bust),99)]
    waistImp = impressions["Waist"][min(int(waist),99)]
    hipImp = impressions["Hip"][min(int(hip),99)]
    finalScore = (cupImp + bustImp + waistImp + hipImp) / 4
    return int(finalScore)

def rank(score):
    count = 0
    predictions = celebsPredectionsSortedFile.readlines()
    for prediction in predictions:
        name, predictedScore  = prediction.strip().split(' ')
        if score < int(predictedScore):
            count += 1
        else:
            return max(1,int(float(count)/float(len(predictions)) * 100))

def competition(score):
    celebrities = []
    predictions = celebsPredectionsFile.readlines()
    for prediction in predictions:
        name, predictedScore  = prediction.strip().split(' ')
        if score >= int(predictedScore):
            celebrities.append(name)
            if len(celebrities) == 5:
                return celebrities

print("Please enter your body measurments in this order [Cup Bust Waist Hip]")
score = score(convert(raw_input()))
print(intro(score) + ", You scored " + str(score) + "%. " + "You're in the top " + str(rank(score)) + "% of all celebrities" + " and ranked with propability higher than or equal to " + celebritiesList(competition(score)))

