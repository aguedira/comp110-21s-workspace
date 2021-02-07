"""An exercise in remainders and boolean logic."""

__author__ = "730212606"


# Begin your solution here...

y: int = int(input("Enter an int: "))


if y % 2 == 0 and y % 7 == 0: 
    print("TAR HEELS.")
else: 
    if y % 2 == 0:
        print("TAR.")
    else: 
        if y % 7 == 0: 
            print("HEELS.")
        else: 
            print("CAROLINA.")

