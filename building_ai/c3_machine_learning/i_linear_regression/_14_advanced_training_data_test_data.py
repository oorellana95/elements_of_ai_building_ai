"""
Exercise 14 (intermediate): Training data vs test data

Write a program that reads data about one set of cabins (training data), estimates linear regression coefficients based on it, then reads data about another set of cabins (test data), and predicts the prices in it. Note that both data sets contain the actual prices, but the program should ignore the prices in the second set. They are given only for comparison.

The contents of the sets are as follows.
https://buildingai.elementsofai.com/Machine-Learning/linear-regression

You can read the data into the program the same way as in the previous exercise.

You should then separate the feature and price data that you have just read from the file into two separate arrays
names x_train and y_train, so that you can use them as argument to np.linalg.lstsq.

The program should work even if the number of features used to describe the cabins differs from five (as long as the
same number of features are given in each file).

The output should be the set of coefficients for the linear regression and the predicted prices for the second set of
cabins."""


import numpy as np
from io import StringIO

train_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

test_string = '''
36 3 15 1 850 196000
75 5 18 2 540 290000
'''


def main():
    np.set_printoptions(precision=1)  # this just changes the output settings for easier reading

    # Training the data
    input_train_file = StringIO(train_string)
    train_data = np.genfromtxt(input_train_file, skip_header=0)
    x_train = np.asarray(train_data[:, :-1])  # input data to the linear regression
    y_train = np.asarray(train_data[:, -1])  # real output
    c = np.linalg.lstsq(x_train, y_train, rcond=-1)[0]  # coefficients of the linear regression

    # Testing the data
    input_test_file = StringIO(test_string)
    test_data = np.genfromtxt(input_test_file, skip_header=0)
    x_test = np.asarray(test_data[:, :-1])  # test data to the linear regression

    # print out the linear regression coefficients
    print(c)

    # this will print out the predicted price for the two new cabins in the test data set
    print(x_test @ c)


main()
