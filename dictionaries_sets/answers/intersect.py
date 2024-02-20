"""
Program name: intersect.py

Description:

This program contains a function named intersect which accepts 2 dictionaries containing key, value pairs of type
{"String", integer} as parameters. The function returns a dictionary containing the set of elements contained in both
dictionaries.

Author: Rae Harbird
This problem is from the exercises in Chapter 8, Building Python Programs, Allison Obourn, Stuart Reges and
Marty Stepp

#Date: August 2018
"""


def intersect(dictionary1, dictionary2):
    the_intersection = {}
    for k, v in dictionary1.items():
        if k in dictionary2:
            if v == dictionary2[k]:
                the_intersection[k] = v

    return the_intersection


def main():
    d1 = {"Janet": 87, "Logan": 62, "Whitaker": 46, "Alyssa": 100, "Stef": 80, "Jeff": 88, "Kim": 52, "Sylvia": 95}
    d2 = {"Logan": 62, "Kim": 52, "Whitaker": 52, "Jeff": 88, "Stef": 80, "Brian": 60, "Lisa": 83, "Sylvia": 87}

    print("Intersection: ", intersect(d1, d2))


if __name__ == "__main__":
    main()
