"""Fortune cookie exercise redux as a structured program."""

from random import randint
__author__ = "730212606"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    # TODO 2: print(fortune_cookie)
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


# TODO 1: def fortune_cookie() -> str:
def fortune_cookie() -> str:
    """The fortune cookie's second line."""
    your_fortune: int = randint(10, 40)
    if your_fortune < 10: 
        if your_fortune < 5:
            return("You're going to struggle before rising back up.")
        else: 
            return("You're going to have one wonderful, perfect day.")
    else: 
        if your_fortune <= 20:
            return("You'll meet the love of your life on a Tuesday evening.")
        else: 
            return("You'll see someone you've forgotten about.")
# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 


if __name__ == "__main__":
    main()