"""
Name: question_5.py
Description: This program tells the user whether or not they have won tickets for a concert.

Author: Rae Harbird
This problem was created by Rob Miller, DIS, UCL for a Java course.

Date: August 2018
"""
from random import *


def main():
    lottery_result = randrange(15) + 1   # Will generate a result between 1 and 15

    # Note: any numbers in the range could be chosen to represent the winning options
    if lottery_result < 5:      # lottery_result is 1, 2, 3 or 4
        number_of_tickets = 1
    elif lottery_result < 7:    # lottery_result is 5 or 6
        number_of_tickets = 2
    elif lottery_result == 7:   # lottery result is 7
        number_of_tickets = 3
    else:
        number_of_tickets = 0
    
    print(f"You have won {number_of_tickets} ticket", end="")
    print("s" if number_of_tickets != 1 else "") 


if __name__ == "__main__":
    main()
