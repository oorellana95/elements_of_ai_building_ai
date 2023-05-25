"""
Exercise 14 (intermediate): Training data vs test data

The program estimates the coefficients of a linear regression model (array c) from the following data:
https://buildingai.elementsofai.com/Machine-Learning/linear-regression

Use the predicted coefficients to obtain price estimates for the following two cabins:
https://buildingai.elementsofai.com/Machine-Learning/linear-regression

Note that the predicted prices will not be the same as the actual prices (which are given in the above table just for
comparison – you won't need them in the exercise).
"""

import numpy as np


def main():
    np.set_printoptions(precision=1)  # this just changes the output settings for easier reading
    x_train = np.array(
        [
            [25, 2, 50, 1, 500],
            [39, 3, 10, 1, 1000],
            [13, 2, 13, 1, 1000],
            [82, 5, 20, 2, 120],
            [130, 6, 10, 2, 600],
            [115, 6, 10, 1, 550]
        ]
    )

    y_train = np.array([127900, 222100, 143750, 268000, 460700, 407000])

    x_test = [
        [36, 3, 15, 1, 850],
        [75, 5, 18, 2, 540]
    ]

    c = np.linalg.lstsq(x_train, y_train, rcond=-1)[0]

    print(x_test @ c)


main()
