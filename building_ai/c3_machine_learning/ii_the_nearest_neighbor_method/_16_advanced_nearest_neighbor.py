"""
Exercise 16 (intermediate): Nearest neighbor

In the basic nearest neighbor classifier, the only thing that matters is the class label of the nearest neighbor. But
the nearest neighbor may sometimes be noisy or otherwise misleading. Therefore, it may be better to also consider the
other nearby data points in addition to the nearest neighbor.

This idea leads us to the so called k-nearest neighbor method, where we consider all the k nearest neighbors. If k=3,
for example, we'd take the three nearest points and choose the class label based on the majority class among them.

The program below uses the library sklearn to generate a random dataset. You don't need to be familiar with sklearn,
we explain all the necessary information below. Each sample in the dataset has two input features (X) and one binary
output class (y). We can think of a sample as a cabin, with its size and price as its input features, and whether we
like it (1) or not (0) as its output class.

The program first generates the random dataset and splits it into training and test sets. Then, for each cabin in the
test set, it identifies its nearest neighbor (k=1) from the cabins in the train set using the distance function.
However, the program has very high standards and dislikes all the cabins y_predict[i] = 0.

Your goal is to make the program smarter by predicting the output class (y_predict) for each cabin in the test set
based on the majority output class (y_train) of its three nearest neighbor (k=3).
"""

import numpy as np
from sklearn.datasets import make_blobs
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# create random data with two classes
X, Y = make_blobs(n_samples=16, n_features=2, centers=2, center_box=(-2, 2))

# scale the data so that all values are between 0.0 and 1.0
X = MinMaxScaler().fit_transform(X)

# split two data points from the data as test data and
# use the remaining n-2 points as the training data
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=2)

# place-holder for the predicted classes
y_predict = np.empty(len(y_test), dtype=np.int64)

# produce line segments that connect the test data points
# to the nearest neighbors for drawing the chart
lines = []


# distance function
def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi) ** 2
    return np.sqrt(sum)


def main(X_train, X_test, y_train, y_test):
    global y_predict
    global lines

    k = 3  # classify our test items based on the classes of 3 nearest neighbors

    # process each of the test data points
    for i, test_item in enumerate(X_test):
        # calculate the distances to all training points
        distances = [dist(train_item, test_item) for train_item in X_train]
        nearest_k_points = np.argsort(distances)[:k]
        y_nearest_k_points = y_train[nearest_k_points]
        y_predict[i] = np.bincount(y_nearest_k_points).argmax()

        # plot
        for nearest_k_point in nearest_k_points:
            lines.append(np.stack((test_item, X_train[nearest_k_point])))

    print(y_predict)


main(X_train, X_test, y_train, y_test)


