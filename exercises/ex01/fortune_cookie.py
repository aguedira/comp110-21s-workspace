"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730212606"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint
x: int = randint(1, 15)
print(x)

# Begin your solution here...

if x < 7: 
    print("Your fortune cookie says...")
else: 
    if x <= 10:
        print("You'll meet the love of your life on a Tuesday evening.")
    else: 
        print("Now, go spread positive vibes.")
