"""
Exercise 10 (intermediate): Naive Bayes classifier

Let's suppose you have a social media account on Instagram, Twitter, or some other platform. (Just in case you don't,
it doesn't matter. We'll fill you in with the relevant information.) You check your account and notice that you have
a new follower – this means that another user has decided to start following you to see things that you post. You
don't recognize the person, and their username (or "handle" as it's called) is a little strange: John37330190. You
don't want to have creepy bots following you, so you wonder. To decide whether you should block the new follower,
you decide to use the Bayes rule!

Suppose we know the probability that a new follower is a bot. You'll be writing a program that takes this value as an
input. For now, let's just call this value P(bot). You'll also be given the probability that the username of a bot
account includes an 8-digit number, which we'll call P(8-digits | bot), as well as the same probability for human (
non-bot) accounts, P(8-digits | human).

To use the Bayes rule, we'll also need to know the probability that a new follower (can be either bot or human) has
an 8-digit number in their username, P(8-digits). The nice thing is that we can calculate P(8-digits) from the above
information. The formula is as follows:

P(8-digits) = P(8-digits | bot) x P(bot) + P(8-digits | human) x P(human) Remember that you can get P(human) simply
as 1–P(bot), since these are the only options. (We consider business and other accounts as "human" as long as they

aren't bots.)

Write a program that takes as input the probability of a follower being a bot (pbot), the probability of a bot having
a username with 8 digits (p8_bot), and the probability of a human having a username with 8 digits (p8_human). The
values for these inputs are free for you to choose, but they have to be probabilitites, so they have to be between 0
and 1.

Using the numbers you give the program calculate P(8-digits) and then use it and the Bayes rule to calculate and
print out the probability of the new follower being a bot, P(bot | 8-digits):

P(bot | 8-digits) =  P(8-digits | bot) x P(bot) / P(8-digits).
"""


def flip(n):
    odds = 1.0         # start with 50% chance of the magic coin, which is the same as odds = 1:1
    p_heads_magic = 1.0
    p_heads_normal = 0.5
    r = p_heads_magic / p_heads_normal
    odds = odds * r**n
    print(odds)


n = 3
flip(n)

