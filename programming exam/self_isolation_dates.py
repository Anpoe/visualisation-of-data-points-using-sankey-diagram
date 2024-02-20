#!/usr/bin/env python3
"""
Program name: self_isolation_dates.py
Student number: 20021899

Given a string and a duration in days, check if the string contains a valid date and compute date when isolation ends by adding the duration specified.
"""

from datetime import datetime
from datetime import timedelta
    

def split_date_f(date):
    """ split "date" using "/" or "-"
    paramaters:
        split_date: str
                    store str tuple value of dates
    arg:
        date: tuple 
                List of unprocessed dates

    returns:
        split_date: str
                    return str tuple value of dates
    """
    # split "date" using "/" or "-"
    split_date = date.split('/')
    if len(split_date) == 1:
        split_date = date.split('-')
        return split_date
    return split_date


def process_date_Y(date, duration):
    """ Change string to date format
    paramaters:
        split_date: str
                    store str tuple value of dates
        true_date: date type
                    store dates 
    arg:
        duration: int
                value added to the date
        date: tuple 
                List of unprocessed dates

    returns:
        split_date: str
                    return str tuple value of dates
        [0, 0, 0]:
                    tuple int [0, 0, 0]
                    as determinate for "incorrect answer"
    """
    # If the separator is "/", the string will be changed to date format
    if "/" in date:
        true_date = datetime.strptime(date, "%d/%m/%Y")
        true_date = true_date + timedelta(days = duration)
        split_date = datetime.strftime(true_date, "%d/%m/%Y")
        split_date = split_date.split('/')
        return split_date
    # If the separator is "-", the string will be changed to date format
    elif "-" in date:
        true_date = datetime.strptime(date, "%d-%m-%Y")
        true_date = true_date + timedelta(days = duration)
        split_date = datetime.strftime(true_date, "%d-%m-%Y")
        split_date = split_date.split('-')
        return split_date
    else:
        return [0, 0, 0]

def process_date_y(date, duration):
    """ Change string to date format
    paramaters:
        split_date: str
                    store str tuple value of dates
        true_date: date type
                    store dates 
    arg:
        duration: int
                value added to the date
        date: tuple 
                List of unprocessed dates

    returns:
        split_date: str
                    return str tuple value of dates
        [0, 0, 0]:
                    tuple int [0, 0, 0]
                    as determinate for "incorrect answer"
    """

    # If the separator is "/", the string will be changed to date format
    if "/" in date:
        true_date = datetime.strptime(date, "%d/%m/%y")
        true_date = true_date + timedelta(days = duration)
        split_date = datetime.strftime(true_date, "%d/%m/%Y")
        split_date = split_date.split('/')
        return split_date
    # If the separator is "-", the string will be changed to date format
    elif "-" in date:
        true_date = datetime.strptime(date, "%d-%m-%y")
        true_date = true_date + timedelta(days = duration)
        split_date = datetime.strftime(true_date, "%d-%m-%Y")
        split_date = split_date.split('-')
        return split_date  
    else:
        return [0, 0, 0]


def self_isolation_end_date(date, duration):
    """ main process function
    paramaters:
        split_date: str
                    store str tuple value of dates
    arg:
        duration: int
                value added to the date
        date: tuple 
                List of unprocessed dates

    returns:
        date: str
                    return str tuple value of dates
        [0, 0, 0]:
                    tuple int [0, 0, 0]
                    as determinate for "incorrect answer"
    """

    # call split_date function and set a variable "split_date"
    split_date = split_date_f(date)
    # determine if the date format is correct
    if len(split_date[0]) <= 2 and split_date[0].isdigit():
        if len(split_date[1]) <= 2 and split_date[1] != '0':
            if len(split_date[2]) == 4:
                if len(split_date) == 3:
                    #if all True, call function "process_date_Y(date, duration)"
                    date = process_date_Y(date, duration)
                    return date

                # return error massage
                else:
                    return [0, 0, 0]

            elif len(split_date[2]) == 2:
                if len(split_date) == 3:
                    #if all True, call function "process_date_y(date, duration)"
                    date = process_date_y(date, duration)
                    return date

            # return error massage
            else:
                return [0, 0, 0]
        else:
            return [0, 0, 0]
    else:
        return [0, 0, 0]




def main():
    ######################################################################################################
    # WARNING: An error will be raised by this code until you define the function self_isolation_end_date 
    ######################################################################################################
    
    # Example cases (dates, duration assumed to always be 10 days)
    correct_dates = ["28/02/2022", "28/2/2022", "28-02-2022", "28/2/22"]
    incorrect_dates = ["128/02/2022", "28/0/2022", "28-02-022", "28/2/22001", "2a/1/19", "1/1/2022/2"]
    
    # Check test cases (i.e., compute end of isolation for these dates)
    for date in correct_dates : 
        result = self_isolation_end_date (date, 10)
        if (result [0] == 0 or result [1] == 0 or result [2] == 0 ) :
            print("Incorrect date")
        else :
            print(f'End isolation in {result [0]} of month {result [1]} of {result[2]}')       
    for date in incorrect_dates : 
        result = self_isolation_end_date (date, 10)
        if (result [0] == 0 or result [1] == 0 or result [2] == 0 ) :
            print("Incorrect date")
        else :
            print(f'End isolation in {result [0]} of month {result [1]} of {result[2]}')   

    
if __name__ == "__main__":
    main()