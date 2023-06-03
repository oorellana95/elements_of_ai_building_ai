"""
Exercise 17 (advanced): Bag of Words

Your task is to write a program that calculates the distances (or differences) between every pair of lines in the
This Little Piggy rhyme and finds the most similar pair. Use the Manhattan distance (also called Taxicab distance) as
your distance metric.

You can start by building a numpy array to store all the distances. Notice that the diagonal elements in the array (
elements at positions [i, j] with i=j) will be equal to zero. This happens because the program will compare every row
also with itself. To avoid selecting those elements, you can assign the value np.inf (the maximum possible floating
point value). To do this, it's necessary to make sure the type of the array is float. Do not use np.float to set the
type of the array, as it is deprecated. Use Python's built-in type float instead.

A quick way to get the index of the element with the lowest value in a 2D array (or in fact, any dimension) is by the
function

np.unravel_index(np.argmin(dist), dist.shape))

where dist is the 2D array. This will return the index as a list of length two.
"""
import numpy as np


data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]


def distance(row1, row2):
    return sum([abs(x-y) for x, y in zip(row1, row2)])


def find_nearest_pair(data):
    # Initialize the variables
    N = len(data)
    dist = np.empty((N, N), dtype=float)

    for ix1, row1 in enumerate(data):
        # Assign the value np.inf as the exercised said
        dist[ix1, ix1] = np.inf

        for ix2, row2 in enumerate(data[ix1+1:]):
            # Calculate the distance
            dist_sum = distance(row1, row2)

            # Assign the value into the 2D array of distances
            dist[ix1, ix1+ix2+1] = dist_sum
            dist[ix1+ix2+1, ix1] = dist_sum

    # Print the index of the element with the lowest value in a 2D array
    print(np.unravel_index(np.argmin(dist), dist.shape))


find_nearest_pair(data)
