"""
Exercise 10 (beginner): Naive Bayes classifier

We have two dice in our desk drawer. One is a normal, plain die with six sides. Each of the sides comes up with an
equal 1/6 probability. The other one is a loaded die that also has six sides, but that however gives the outcome six
on every second try on average. That means the probability that you get a six is 16.7% with the first die but 50%
with the second die.

Suppose that we pick one of the dice at random so that both have the same chances of being picked, then start rolling
the same die again and again. If the outcome is six on the first roll, you wouldn't be very sure it's the loaded die.
If the outcome is also six on the second roll, you'd start thinking it probably is. After the third six, you'd start
to be quite convinced.

If the outcome keeps being six, how many rolls would it take altogether (counting from the start) until the odds are
at least 100:1 in favor of the loaded die?

Tip: use the likelihood ratio (r) discussed above. In this case, r = P(6 | loaded) / P(6 | normal).
"""

"""
Answer: 

The likelihood ratio is r = P(6 | loaded) / P(6 | normal) = (1/2) / (1/6) = 3. If we start with the odds 
1:1, the sequence of odds after each roll with the outcome 6 are as follows: 3:1, 9:1, 27:1, 81:1, 243:1, 
... The fifth one is the first that is 100:1 or higher, so it takes five rolls with the outcome 6 to reach 100:1.
"""

