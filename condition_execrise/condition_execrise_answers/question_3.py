"""
Name: question_3.py
Description:

This program calculates the christmas bonus based upon the number of years of service an employee has accrued

Author: Rae Harbird
This problem was created by Rob Miller, DIS, UCL for a Java course.

Date: August 2018
"""

BASIC_BONUS = 50


def main():
    
    bonus = BASIC_BONUS
    
    years_service = int(input("How many years have you been with the company? "))
    
    if years_service >= 20:
        bonus += 100
    elif years_service >= 10:
        bonus += 50
    
    print(f"You will receive a Christmas bonus of {bonus} pounds")


if __name__ == "__main__":
    main()
