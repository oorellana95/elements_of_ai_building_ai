"""In this exercise you need to list all the possible routes that start from Panama and visit each of the other ports exactly once.

The template code below contains an incomplete permutations function which takes as input a specified route and a list of port names absent from that route. Modify the function so that it prints out all the possible orderings of the ports that always begin with Panama (PAN).

The mathematical term for such orderings is a permutation. Note that your program should work for an input portnames list of any length. The order in which the permutations are printed doesn't matter.

As the output the function should print each permutation on its own row, as one string, with the port names separated by spaces. For this, you can use the join function as follows: print(' '.join([portnames[i] for i in route]))."""

import itertools

port_names = ["PAN", "AMS", "CAS", "NYC", "HEL"]


def permutations(route, ports):
    # Write your recursive code here
    for i in itertools.permutations(ports):
        route = [0] + list(i)
        print(' '.join([port_names[i] for i in route]))


# This will start the recursion with 0 ("PAN") as the first stop
permutations([0], list(range(1, len(port_names))))


# Given solution
def permutations_solution(route, ports):
    if len(ports) < 1:
        print(' '.join([port_names[i] for i in route]))
    else:
        for i in range(len(ports)):
            permutations_solution(route + [ports[i]], ports[:i] + ports[i + 1:])


permutations_solution([0], list(range(1, len(port_names))))