import random


def lang() -> None:
    """Language config"""
    try:
        lang_choice: int = int(input("Choose your language: [1]=EN [2]=RU:"))
    except ValueError:
        print("Choose your language: [1]=EN [2]=RU")
    else:
        if lang_choice == 1:
            pass
        else:
            pass


def err() -> None:
    """Check for win"""
    if choice == random.randint(1, 3):
        print("Congratulations! You won!")
    else:
        print("Sorry, you didn't guess. Try again!")


if __name__ == "__main__":
    print("Welcome to THE GAME OF THIMBLES v.0.1.0 by dendyua")

    # Language set
    lang()

    # Main loop
    while True:
        try:
            # Check input for integer from 1 to 3
            choice: int = int(input("Please enter the thimble number (from 1 to 3):"))
        except ValueError:
            print("You need to enter a number from 1 to 3")
        else:
            if 1 <= choice <= 3:
                # Check for win
                err()
            else:
                print("You need to enter a number from 1 to 3")
