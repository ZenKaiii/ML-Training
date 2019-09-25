import numpy as np
from math import sqrt
from collections import Counter

def kNN_classify(k, X_train, y_train, x):

    assert 1<=k<=X_train.shape[0],"k必须合法"
    assert X_train.shape[0] == y_train.shape[0],\
        "X_train 样本个数等于 y_train"
    assert X_train.shape[1] == x.shape[0],\
        "x特征数等于 X_train"

    distances = [sqrt(np.sum((x_train - x)**2)) for x_train in X_train]
    nearest = np.argsort(distances)
    topK_y = [y_train[i] for i in nearest[:k]]
    votes = Counter(topK_y)
    return votes.most_common()[0][0]