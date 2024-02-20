"""
Name: symmetric_set_difference.py
Description:

This program contains a function named 'symmetric_set_difference' which accepts 2 sets of integers as parameters.
The function returns a new set containing their symmetric set difference (that is, the set of elements contained in
either of the two sets but not in both). For example, the symmetric difference between the sets {1, 4, 7, 9} and
{2, 4, 5, 6, 7} is {1, 2, 5, 6, 9}.

Author: Rae Harbird
This problem is from the exercises in Chapter 8, Building Python Programs, Allison Obourn, Stuart Reges and
Marty Stepp

Date: August 2018
"""


def symmetric_set_difference(set1, set2):
    set3 = set1.difference(set2).union(set2.difference(set1))
    return set3


def main():
    s1 = {1, 4, 7, 9}
    s2 = {2, 4, 5, 6, 7}
    print("Symmetric set difference:")
    print("s1:", s1)
    print("s2:", s2)
    print("SSD: ", symmetric_set_difference(s1, s2))


if __name__ == "__main__":
    main()
