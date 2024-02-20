"""
Name: question_2.py
Description:

This program prompts the user for their age and tells them whether they may do jury service.

Author: Rae Harbird
This problem was created by Rob Miller, DIS, UCL for a Java course.

Date: August 2018
"""


def main():
    age = int(input("Enter your age: "))
    criminal_record = input("Do you have a criminal record y/n: ")

    if age <= 0 or (criminal_record != 'y' and criminal_record != 'n'):
        print("\nIncorrect input")
    else:
        if age >= 18 and criminal_record.lower() == 'n':
            print("\nYou are required to do jury service.")
        else:
            print("\nYou are excluded from jury service.")
            
            
if __name__ == "__main__":
    main()
