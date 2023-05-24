"""
Exercise 11 (intermediate): Real estate price predictions

Edit the code so that it prints out the prices of multiple cabins in one go.
"""


# input values for three mökkis:
#  - size [m^2],
#  - size of the sauna [m^2],
#  - distance to water [m],
#  - number of indoor bathrooms,
#  - proximity of neighbors [m]
X = [[66, 5, 15, 2, 500],
     [21, 3, 50, 1, 100],
     [120, 15, 5, 2, 1200]]

# coefficient values
c = [3000, 200, -50, 5000, 100]


def predict(X, c):
    for x in X:
        price = c[0] * x[0] + c[1] * x[1] + c[2] * x[2] + c[3] * x[3] + c[4] * x[4]
        print(price)


predict(X, c)

