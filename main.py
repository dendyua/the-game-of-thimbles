import random

print("Welcome to THE GAME OF THIMBLES v.0.1.0 by dendyua")

boils = [1, 2, 3]


def lang():
    try:
        lang_chois = int(input("Choose your language: [1]=EN [2]=RU:"))
    except ValueError:
        print("Choose your language: [1]=EN [2]=RU")
    else:
        if lang_chois == 1:
            pass
        else:
            pass


def err():
    if chois == boils[0]:
        print("Congratulations! You won!")
    else:
        print("Sorry, you didn't guess. Try again!")


lang()
while True:
    random.shuffle(boils)
    try:
        chois = int(input("Please enter the thimble number (from 1 to 3):"))
    except ValueError:
        print("You need to enter a number from 1 to 3")
    else:
        if 1 <= chois <= 3:
            err()
        else:
            print("You need to enter a number from 1 to 3")
