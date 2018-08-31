celebsFeaturesFile = open("gdValues.txt", "r")

lines = celebsFeaturesFile.readlines()
mean_x1, mean_x2, mean_y = lines[0].strip().split(' ')
std_x1, std_x2, std_y = lines[1].strip().split(' ')
theta_0, theta_1, theta_2 = lines[2].strip().split(' ')

tobePredictedBust = 38.0

for predict in [34,36,38,40,100]:
    x1 = float(predict)
    x2 = float(predict) * float(predict)
#    x1 = (float(predict) - float(mean_x1)) / float(std_x1)
#    x2 = ((float(predict) * tobePredictedBust) - float(mean_x2)) / float(std_x2)
    Y = float(theta_0) + float(theta_1) * x1 + float(theta_2) * x2
    finalY = (Y * float(std_y)) + float(mean_y)
    print(x1,mean_x1, std_x1)
    print(x2,mean_x2, std_x2)
    print(Y,mean_y, std_y)
    print(predict, finalY)

#old = new * std + mean
#new = (old - mean)/std



