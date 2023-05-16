"""
Exercise 5 (advanced): Warm-up Temperature

Suppose the current solution has score S_old = 150 and you try a small modification to create a new solution with score
S_new = 140. In the greedy solution, this new solution wouldn't be accepted because it would mean a decrease in the
score. In simulated annealing, the new solution is accepted with a certain probability as explained above.

Modify the accept_prob function so that it returns the probability of accepting the new state using simulated annealing.
The program should take the two score values (the current and the new) and the temperature value as arguments.
"""

import random
import numpy as np


# It fails because some decimals between numpy and math modules
def accept_prob_failed(S_old, S_new, T):
    if S_new > S_old:
        return 1.0
    return np.exp(-(S_old-S_new)/T)


# It is the solution
def accept_prob(S_old, S_new, T):
    if S_new > S_old:
        return 1.0
    return np.exp(-(S_old-S_new)/T)


def accept(S_old, S_new, T):
    if random.random() < accept_prob(S_old, S_new, T):
        print(True)
    else:
        print(False)


accept(S_old=150, S_new=140, T=5)