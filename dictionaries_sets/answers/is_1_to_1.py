"""

Program name: is_1_to_1.py

Description:

This program contains a function named is_1_to_1 which accepts a dictionary of key, value pairs
as a parameter and returns True or False. The problem illustrates the use of dictionary comprehensions. If a
dictionary has a key which maps to 2 or more entries then the reverse dictionary will have fewer entries because
the keys in the dictionary will be unique.

True is returned if no two keys map to the same value.
True is returned if the dictionary is empty.
False is returned if at least one key maps to the same value as another.


Author: Rae Harbird
This problem is from the exercises in Chapter 8, Building Python Programs, Allison Obourn, Stuart Reges and
Marty Stepp

Date: August 2018
"""


def is_1_to_1(the_dictionary):

    reverse_dictionary = {}
    for k, v in the_dictionary.items():
        reverse_dictionary[v] = k

    if len(the_dictionary) == 0 or \
       (len(reverse_dictionary) == len(the_dictionary)):
        return True
    else:
        return False


def main():
    d1 = {"Marty": "206-9024", "Hawking": "123-4567", "Smith": "949-0504", "Newton": "123-4567"}
    d2 = {"Marty": "206-9024", "Hawking": "555-1234", "Smith": "949-0504", "Newton": "123-4567"}
    d3 = {}
    for d in [d1, d2, d3]:
        if is_1_to_1(d):
            print("\nDictionary: ", d, "has unique entries.")
        else:
            print("\nDictionary: ", d, "does not have unique entries.")


if __name__ == "__main__":
    main()
