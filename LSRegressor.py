import numpy as np
from numpy.linalg import inv

class LSRegressor(object):

    def __init__(self):
        pass

    def train(self, X, Y):
        """ X is N x D where each row is an example. Y is 1-dimension of size N """
        self.x_train = X
        self.y_train = Y
        x_t = self.x_train.T
        self.w = ((inv((x_t).dot(self.x_train))).dot(x_t)).dot(self.y_train)
        self.w = np.reshape(self.w, (self.w.shape[0], -1))
        
            

    def predict(self, X):
        """ X is N x D where each row is an example we wish to predict label for """

        num_test = X.shape[0]
        # lets make sure that the output type matches the input type
        Ypred = np.zeros(num_test, dtype = self.y_train.dtype)
        # loop over all test rows
        for i in range(num_test):            
            result = (self.w.T).dot(X[i,:].reshape(self.w.shape))
            Ypred[i] = result
        return Ypred
