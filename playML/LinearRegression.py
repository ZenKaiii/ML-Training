import numpy as np
from metrics import r2_score

class LinearRegression():
    def __init__(self):
        self.coef_ = None
        self.intercept_ = None
        self._theta = None

    def fit_normal(self, X_train, y_train):
        assert X_train.shape[0] == y_train.shape[0]
        X_b = np.hstack([np.ones((len(X_train),1)),X_train])
        self._theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y_train)

        self.intercept_ = self._theta[0]
        self.coef_ = self._theta[1:]
        return self

    def fit_gd(self,X_train, y_train, eta =0.01, n_iters=1e4):
        assert X_train.shape[0] == y_train.shape[0]

        def J(theta, X_b ,y):
            try:
                return np.sum((y - X_b.dot(theta))**2) / len(y)
            except:
                return float('inf')

        def dJ(theta, X_b, y):
            res = np.empty(len(theta))
            res[0] = np.sum(X_b.dot(theta) - y)
            for i in range(1,len(theta)):
                res[i] = (X_b.dot(theta) - y).dot(X_b[:,i])
            return res*2/len(X_b)
        def gradient_descent(X_b, y, initial_theta, eta, n_iters=1e4, epsilon=1e-8):
            theta = initial_theta
            cur_iter = 0
            while cur_iter < n_iters:
                gradient = dJ(theta,X_b,y)
                last_theta = theta
                theta = theta - eta * gradient
                if(abs(J(theta,X_b,y) - J(last_theta,X_b,y)) < epsilon):
                    break
                cur_iter+=1
            return theta

        X_b = np.hstack([np.ones((len(X_train),1)),X_train])
        initial_theta = np.zeros(X_b.shape[1])
        self._theta = gradient_descent(X_b,y_train,initial_theta,eta)
        self.intercept_ = self._theta[0]
        self.coef_ = self._theta[1:]

    def predict(self,X_predict):
        assert self.intercept_ is not None and self.coef_ is not None
        assert X_predict.shape[1] == len(self.coef_)

        X_b = np.hstack([np.ones((len(X_predict),1)),X_predict])
        return X_b.dot(self._theta)

    def score(self,X_test,y_test):
        y_predict = self.predict(X_test)
        return r2_score(y_predict,y_test)

    def __repr__(self):
        return "LinearRegression()"