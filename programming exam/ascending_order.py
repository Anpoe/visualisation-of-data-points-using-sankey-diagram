#!/usr/bin/env python3
""" 
Program name: ascending_order.py
Student number: 20021899

Given a 2D list, remove out of order entries.
"""
from os import remove
from turtle import up


def ascending_order_multi(citizen_cases):
    """Remove out of order updates out of a list of lists of updates

       Args:
            citizen_cases (list): List of citizens cases, each of them containing a nested list with the citizen's updates 

       return:
            citizen_cases (list): List of citizens cases, sorted and delete unnecessary numbers,
            each of them containing a nested list with the citizen's updates 
    """
    # Insert your code here

    # for loop to travel throughout the list in the lists
    for n in citizen_cases:
        # set counter as a stop determinate
        counter = 1
        # for loop to travel throughout the number in lists
        for i in n:                
            
            while counter < len(n):
                # If the number after is smaller than the one before, delete it
                if n[counter] < n[counter - 1]:
                    del n[counter]
                else:
                    counter += 1
    return citizen_cases


def ascending_order(updates):
    """Remove out of order entries of the list of updates.

    Args:
        updates (list): List from which zeroes will be removed.
    """
    # Insert your code here

    # set counter as a stop determinate  
    counter = 1
    # while loop to travel throughout the number in lists
    while counter < len(updates):
        # If the number after is smaller than the one before, delete it
        if updates[counter] < updates[counter - 1]:
            del updates[counter]
        else:
            counter += 1
    return updates      
    

def main():
    lis_1 = [0, 2, 6, 0, 23, 8, 45, 7, 0 ]
    print(lis_1)
    ascending_order (lis_1)
    print("List in ascending order: ", lis_1)

    lis_2 = [[ 1, 34, 45, 6, 124, 0, 134], [0], [0, 930, 0 ]]
    print(lis_2)
    ascending_order_multi(lis_2)
    print("All Lists, each of them in ascending order: ", lis_2)

    
if __name__ == "__main__":
    main()