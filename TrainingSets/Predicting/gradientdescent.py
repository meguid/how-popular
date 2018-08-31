import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def computeCost(X,y,theta):
    tobesummed = np.power(((np.dot(X, theta.T))-y),2)
    return np.sum(tobesummed)/(2 * len(X))

def gradientDescent(X,y,theta,iters,alpha):
    cost = np.zeros(iters)
    for i in range(iters):
        theta = theta - (alpha/len(X)) * np.sum(X * (np.dot(X, theta.T) - y), axis=0)
        cost[i] = computeCost(X, y, theta)
    return theta,cost

my_data = pd.read_csv('impressionsBustTest.txt',names=["bust","bustsq","fans"]) #read the data

#setting the matrixes
X = my_data.iloc[:,0:2]
ones = np.ones([X.shape[0],1])
X = np.concatenate((ones,X),axis=1)
y = my_data.iloc[:,2:3].values #.values converts it from pandas.core.frame.DataFrame to numpy.ndarray
theta = np.zeros([1,3])

#running the gd and cost function
g,cost = gradientDescent(X,y,theta,1000,0.01)
finalCost = computeCost(X,y,g)

theta0 = g[0][0]
theta1 = g[0][1]
theta2 = g[0][2]
print(theta0,theta1, theta2)

for predict in [1,20,34,36,38,40,100]:
    x1 = float(predict) / 100.0
    x2 = float(predict) * float(predict) / 10000.0
    Y = theta0 + theta1 * x1 + theta2 * x2
    finalY = (Y) * 1000
    print(predict, x1, x2, finalY)

fig, ax = plt.subplots()
ax.plot(np.arange(1000), cost, 'r')
ax.set_xlabel('Iterations')
ax.set_ylabel('Cost')
ax.set_title('Error vs. Training Epoch')
plt.show()
