from matplotlib import pyplot as plt
import numpy as np

data = [[3, 1.5, 1], [2, 1, 0], [4, 1.5, 1], [3, 1, 0], [3.5, 0.5, 1], [2, 0.5, 0], [5.5, 1, 1], [1, 1, 0]]

mystery = [4.5, 1]

# weights
w1 = np.random.randn()
w2 = np.random.randn()

# bias
b = np.random.randn()

def sigmoid(x):
    return 1/(1 + np.exp(-x))

def dSigmoid(x):
    return sigmoid(x) * (1 - sigmoid(x))

def graph(formula, x_range):  
    x = np.array(x_range)  
    y = formula(x)
    plt.plot(x, y)

# scatter data
def scatter():
    plt.axis([0, 6, 0, 6])
    plt.grid()
    for i in range(len(data)):
        point = data[i]
        color = 'r'
        if point[2] ==  0:
            color = 'b'
        plt.scatter(point[0], point[1], c=color)

# training loop
learningRate = 0.2
costs = []
for i in range(50000):
    ri = np.random.randint(len(data))
    point = data[ri]

    z = point[0]*w1 + point[1]*w2 + b
    pred = sigmoid(z)

    target = point[2]
    cost = np.square(pred - target)

    if (i % 100 == 0):
        print(cost)
        costs.append(cost)

    dCost = 2 * (pred - target)
    dPred = dSigmoid(z)
    dz_dw1 = point[0]
    dz_dw2 = point[1] 
    dz_db = 1

    dCost_dz = dCost * dPred

    dCost_dw1 = dCost * dz_dw1
    dCost_dw2 = dCost * dz_dw2
    dCost_db = dCost * dz_db

    # update weights and bias
    w1 = learningRate * dCost_dw1
    w2 = learningRate * dCost_dw2
    b = learningRate * dCost_db

plt.clf()
plt.plot(costs)
plt.savefig('costs.png')

plt.clf()
scatter()

zMistery = mystery[0]*w1 + mystery[1]*w2 + b

if(zMistery < 0.5):
    color = 'b'
else:
    color = 'r'

plt.scatter(mystery[0], mystery[1], c=color)
z = w1*x + w2*y + b
plt.plot(x,y,z)
print(w1,w2,b)
plt.savefig("scatter.png")
