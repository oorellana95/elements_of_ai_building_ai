"""
Exercise 15 (intermediate): Vector distance

Which of these calculate the Euclidean distance between two vectors correctly? You can assume that the arrays a and b
containing the vectors are of equal length."""

import numpy as np


# The option A:
def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi)**2
    return np.sqrt(sum)
