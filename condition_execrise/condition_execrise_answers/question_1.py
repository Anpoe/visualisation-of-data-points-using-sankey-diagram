"""
Name: question_1.py
Description:

This program prompts the user for their age and tells them the cost of a cinema ticket.

Author: Rae Harbird
This problem was created by Rob Miller, DIS, UCL for a Java course.

Date: August 2018
"""

FULL_TICKET_PRICE = 6.00


def main():

    age = int(input("Enter your age: "))
    if age >= 60:
        ticket_price = FULL_TICKET_PRICE / 3
    elif age < 16:
        ticket_price = FULL_TICKET_PRICE / 2
    else:
        ticket_price = FULL_TICKET_PRICE
        
    print(f"Your ticket costs {ticket_price:.2f}.")


if __name__ == "__main__":
    main()
