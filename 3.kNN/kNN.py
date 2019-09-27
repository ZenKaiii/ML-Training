import numpy as np
from math import sqrt
from collections import Counter

# def kNN_classify(k, X_train, y_train, x):
#
#     assert 1<=k<=X_train.shape[0],"k必须合法"
#     assert X_train.shape[0] == y_train.shape[0],\
#         "X_train 样本个数等于 y_train"
#     assert X_train.shape[1] == x.shape[0],\
#         "x特征数等于 X_train"
#
#     distances = [sqrt(np.sum((x_train - x)**2)) for x_train in X_train]
#     nearest = np.argsort(distances)
#     topK_y = [y_train[i] for i in nearest[:k]]
#     votes = Counter(topK_y)
#     return votes.most_common()[0][0]


class kNNClassifier:
    def __init__(self,k):
        assert k>=1
        self.k = k
        self._X_train = None
        self._y_train = None
    def fit(self,X_train, y_train):
        assert X_train.shape[0] == y_train.shape[0]
        assert self.k <= X_train.shape[0]
        self._X_train = X_train
        self._y_train = y_train
        return self
    def predict(self,X_predict):
        assert self._y_train is not None and self._y_train is not None
        assert X_predict.shape[1] == self._X_train.shape[1]

        y_predict = [self._predict(x) for x in X_predict]
        return np.array(y_predict)

    def _predict(self,x):
        assert x.shape[0] == self._X_train.shape[1]
        distances = [sqrt(np.sum((x_train - x)**2)) for x_train in self._X_train]
        nearest = np.argsort(distances)
        topK_y = [self._y_train[i] for i in nearest[:self.k]]
        votes = Counter(topK_y)
        return votes.most_common(1)[0][0]

    def __repr__(self):
        return "KNN(k=%d)" %self.k