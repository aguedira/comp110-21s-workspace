"""Tar Heels exercise redux as a structured program."""

__author__ = "730212606"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    # TODO 2: print(tar_heels)
    print(tar_heels(choice))


# TODO 1: def tar_heels() -> str
def tar_heels(choice: int) -> str:
    """The program that determines if a number is divisible by 2 and/or 7."""
    if choice % 2 == 0 and choice % 7 == 0: 
        return('TAR HEELS')
    else: 
        if choice % 2 == 0:
            return('TAR')
        else: 
            if choice % 7 == 0: 
                return('HEELS')
            else: 
                return('CAROLINA')


if __name__ == "__main__":
    main()