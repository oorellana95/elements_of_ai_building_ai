"""Write a program that prints "I love" followed by one word: the additional word should be 'dogs' with 80% probability, 'cats' with 10% probability, and 'bats' with 10% probability."""
import random


def main():
    if random.random() < 0.2:
        favourite = 'bats' if random.random() < 0.5 else 'cats'
    else:
        favourite = 'dogs'
    print("I love " + favourite)


main()


def main_solution():
    """Much better since it uses only 1 random.random and 1 if else"""
    x = random.random()
    if x < 0.8:
        favourite = "dogs"
    elif x < 0.9:
        favourite = "cats"
    else:
        favourite = "bats"

    print("I love " + favourite)