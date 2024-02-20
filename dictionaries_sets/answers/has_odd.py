"""
Description:

This program contains a function named 'has_odd' which accepts a set of integers as a parameter. The function returns
True if the set contains at least one odd number and False if it does not.

Author: Rae Harbird
This problem is from the exercises in Chapter 8, Building Python Programs, Allison Obourn, Stuart Reges and
Marty Stepp

#Date: August 2018
"""


def has_odd(the_set):
    is_odd = False
    for n in the_set:
        if n % 2 != 0:
            is_odd = True
    return is_odd


def main():
    s1 = set(list(range(20)))
    s2 = set([n + n for n in s1])
    s3 = set()
    for s in [s1, s2, s3]:
        print(s)
        if has_odd(s):
            print("Set contains odd number")
        else:
            print("Set does not contain odd number")


if __name__ == "__main__":
    main()
