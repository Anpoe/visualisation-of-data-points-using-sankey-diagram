"""
Name: question_6.py
Description: This program prompts the user to enter a year and tells the user whether or not the year is a leap year.

Author: Rae Harbird

Date: August 2018
"""


def main():
    leap = False
    
    year = int(input("Enter a year: "))
    
    if year % 400 == 0:
        leap = True
    elif year % 4 == 0 and year % 100 != 0:
        leap = True
        
    print(f"{year} is ", end="")
    print("" if leap else "not ", end="")
    print("a leap year")


if __name__ == "__main__":
    main()
