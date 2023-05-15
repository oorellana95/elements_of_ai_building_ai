import random, math
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