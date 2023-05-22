"""Building on the previous solution, modify the code so that it finds the route with minimum carbon emissions and prints it out. Again, the program should work for any number of ports. You can assume that the distances between the ports are given in an array of the appropriate size so that the distance between ports i and j is found in D[i][j]."""
import itertools


portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

# https://sea-distances.org/
# nautical miles converted to km

D = [
        [0,8943,8019,3652,10545],
        [8943,0,2619,6317,2078],
        [8019,2619,0,5836,4939],
        [3652,6317,5836,0,7825],
        [10545,2078,4939,7825,0]
    ]

# https://timeforchange.org/co2-emissions-shipping-goods
# assume 20g per km per metric ton (of pineapples)

co2 = 0.020

# DATA BLOCK ENDS

# these variables are initialised to nonsensical values
# your program should determine the correct values for them
smallest = 1000000
bestroute = [0, 0, 0, 0, 0]


def permutations(route, ports):
    global smallest, bestroute
    for i in itertools.permutations(ports):
        route = [0] + list(i)
        distance = D[route[0]][route[1]] + D[route[1]][route[2]] + D[route[2]][route[3]] + D[route[3]][route[4]]
        emissions = distance * co2
        if emissions < smallest:
            bestroute = route
            smallest = emissions


def permutations_solution(route, ports):
    global smallest, bestroute
    if len(ports) < 1:
        score = co2 * sum(D[i][j] for i, j in zip(route[:-1], route[1:]))
        if score < smallest:
            smallest = score
            bestroute = route
    else:
        for i in range(len(ports)):
            permutations_solution(route+[ports[i]], ports[:i]+ports[i+1:])


def main():
    # Do not edit any (global) variables using this function, as it will mess up the testing

    # this will start the recursion
    permutations([0], list(range(1, len(portnames))))

    # print the best route and its emissions
    print(' '.join([portnames[i] for i in bestroute]) + " %.1f kg" % smallest)


main()
