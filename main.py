import random


def lang() -> None:
    try:
        lang_chois: int = int(input("Choose your language: [1]=EN [2]=RU:"))
    except ValueError:
        print("Choose your language: [1]=EN [2]=RU")
    else:
        if lang_chois == 1:
            pass
        else:
            pass


def err() -> None:
    if chois == random.randint(1, 3):
        print("Congratulations! You won!")
    else:
        print("Sorry, you didn't guess. Try again!")


if __name__ == "__main__":
    print("Welcome to THE GAME OF THIMBLES v.0.1.0 by dendyua")

    lang()
    while True:
        try:
            chois: int = int(input("Please enter the thimble number (from 1 to 3):"))
        except ValueError:
            print("You need to enter a number from 1 to 3")
        else:
            if 1 <= chois <= 3:
                err()
            else:
                print("You need to enter a number from 1 to 3")