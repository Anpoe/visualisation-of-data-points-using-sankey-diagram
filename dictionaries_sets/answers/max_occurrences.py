"""
Name: max_occurrences.py
Description:

This program contains a function called max_occurrences that accepts a list of integers as a parameter
and returns a key, value pair which are: the most frequently occurring integer and the number of times
the most frequently occurring integer (the "mode") occurs in the list. Solve this problem using a
dictionary. If the list is empty, return (0,0)..

Author: Rae Harbird
This problem is from the exercises in Chapter 8, Building Python Programs, Allison Obourn, Stuart Reges and
Marty Stepp

Date: August 2018
"""

import random

"""
 max_occurrences(listOfDigits)

 This function takes a list of digits between 0 and 9 and
 returns the most frequently occurring digit and the number
 of times that digit occurred.

 @param listOfDigits is the list containing the digits.
 @return the most frequently occurring digit.
 @return the mode.
"""


def max_occurrences(list_of_digits):
    dictionary_of_digits = {}
    max_occurrence = 0
    mode = 0

    for i in list_of_digits:
        if i in dictionary_of_digits:
            dictionary_of_digits[i] = dictionary_of_digits[i] + 1
        else:
            dictionary_of_digits[i] = 1
    
    for digit, num_occurrences in dictionary_of_digits.items():    # search the dictionary for the associated key
        if num_occurrences > max_occurrence:
            max_occurrence = num_occurrences
            mode = digit
    
    return mode, max_occurrence


"""
 generate_list_of_numbers(listLength)

 This function returns a list of numbers between 0 and 9.
 The length of the list is listLength.
 @param listLength is the length of the list returned.
 @return a list listLength long.
"""


def generate_list_of_numbers(list_length):
    list_of_numbers = []
    
    for i in range(list_length):
        list_of_numbers.append(random.randrange(10))
    return list_of_numbers


def main():
    # Generate a list of 100 numbers
    list_of_digits = generate_list_of_numbers(100)
    most_common_number, occurs = max_occurrences(list_of_digits)
    print("\nList of digits: {}".format(list_of_digits))
    print("\nNumber {} appears most frequently - {} times".format(most_common_number, occurs))
    
    # Now check what happens with an empty list
    list_of_digits = []
    print("\nList of digits: {}".format(list_of_digits))
    most_common_number, occurs = max_occurrences(list_of_digits)
    if most_common_number == 0 and occurs == 0:
        print("List: {} is empty".format(list_of_digits))


if __name__ == "__main__":
    main()
