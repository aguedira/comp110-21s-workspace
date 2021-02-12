"""An exercise in remainders and boolean logic."""

__author__ = "730212606"


# Begin your solution here...

pick_a_number: int = int(input("pick a number: "))


if pick_a_number % 2 == 0 and pick_a_number % 7 == 0: 
    print('TAR HEELS.')
else: 
    if pick_a_number % 2 == 0:
        print('TAR.')
    else: 
        if pick_a_number % 7 == 0: 
            print('HEELS.')
        else: 
            print('CAROLINA.')