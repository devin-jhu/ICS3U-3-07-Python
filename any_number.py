#!/usr/bin/env python3

# Created by Devin Jhu
# Created on April 2022
# The date calculator

import random


def main():
    # this function helps gandma

    print("Are you old enough to date my gradchild")

    # input
    age_string = input("Enter your age: ")

    # process
    try:
        age_number = int(age_string)

        if age_number >= 25 and age_number <= 40:
            print("You may date my grandchild")
        else:
            print("You may NOT date my grandchild")

    except Exception:
        print("Not an age")
    print("\nDone.")


if __name__ == "__main__":
    main()
