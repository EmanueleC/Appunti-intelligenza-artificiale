import numpy as np

class NearestNeighbor:
    def __init__(self):
        pass

    def distance(self, Xtri, Xi):
        return np.sum(np.abs(Xtri - Xi), axis = 0)

    def train(self, X, Y):
        # the nearest neighbor classifier simply remembers all the training data
        self.Xtr = X
        self.Ytr = Y

    def predict(self, X):
        num_test = X.shape[0] # X.shape = [row, column]
        Ypred = np.zeros(num_test, dtype = self.Ytr.dtype)

        for i in range(num_test):
            distances = self.distance(self.Xtr[i], X[i])
            min_index = np.argmin(distances)
            Ypred[i] = self.Ytr[min_index]

        return Ypred

# just playing...
nn = NearestNeighbor()
training_set = np.array([[1,2,3,4,5,6,7,8,9,10],[0,1,0,1,0,1,0,1,0,1]])
test_set = np.array([11,12,13,14,15,16,17])
nn.train(training_set[0],training_set[1])
result = nn.predict(test_set)
print(result)
