"""
Exercise 8: Fishing in the Nordics
Write a program that uses statistics about the population and fishing industry employment to print out conditional
probabilities of each nationality given that the winner works in the fishing industry.

The data is given in lists containing the population and the number of fishers in each country.
"""


def main():
    countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
    fishers = [1891, 2652, 3800, 11611, 1757]

    total_fishers = sum(fishers)

    for country, fisher in zip(countries, fishers):
        probability = fisher / total_fishers * 100
        print("%s %.2f%%" % (country, probability))  # modify this to print correct results


main()
