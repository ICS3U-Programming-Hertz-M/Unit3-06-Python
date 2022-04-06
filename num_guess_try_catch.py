#!/usr/bin/env python3
#
# Created by: Hertz Antonella
# Created on: Apr 5 2022
# This program ask the user to guess any number between 0 and 9
import random


random_variable = random.randint(0, 9)


def main():
    # get user input
    user_number = input("Guess any number from 0 to 9: ")
    print("")

    try:
        # change from string to int
        user_number_as_int = int(user_number)
        # compare the number entered to random_variable
        if user_number_as_int == random_variable:
            print("correct guess!")
        else:
            print("your guess is incorrect,the correct guess is", random_variable)

    except Exception:
        print("{} is not an integer.".format(user_number))
    finally:
        print("play again")


if __name__ == "__main__":
    main()
