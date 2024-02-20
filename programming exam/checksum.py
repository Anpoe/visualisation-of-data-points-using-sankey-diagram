#!/usr/bin/env python3
'''
Program name: checksum.py
Student number: 20021899

Test if the checksum of a lateral flow is correct .
'''

def checksum(test_number):
    """Check the validity and return the checksum of a the 13-digit code identifying a lateral flow test. 
    If the checksum is not correct, it returns a negative checksum number (-1).

    Args:
        test_number (int): 13-digit code to check

    Returns:
        int: 1-digit checksum if code is correct. Returns a negative number (-1) otherwise.
    """
    # Insert your code here (delete proxy code - return -1)

    while True:
        # make int to str
        test_number1 = str(test_number)
        # Initialize variables 
        sum1 = 0
        sum2 = 0
        i = 0

        # Slicing in a string and extract the number, 
        # then sum them up
        for i in test_number1[-1::-2]:
            sum1 += int(i)
        
        #calculation 
        sum1 = sum1 - test_number % 10
        sum1 = sum1 * 7 

        # Slicing in a string and extract the number, 
        # then sum them up
        for i in test_number1[-2::-2]:
            sum2 += int(i)

        #calculation 
        sum2 = sum2 * 2
        sum3 = sum1 + sum2
        sum3 = sum3 % 10

        # Determine if the test_number end is equal to sum3
        if sum3 == test_number % 10:
            return sum3
            
        else:
            return -1

def main():
    correct_examples = [1234567890126, 1234566543219]
    incorrect_examples = [2345677654329, 8928361073766]
    global total
    total = correct_examples + incorrect_examples
    # Check test cases:
    for code in correct_examples :
        checksum_number = checksum(code)
        if(checksum_number >= 0):
            print(f'The checksum of {code} is {checksum_number}')
        else: 
            print (f'The checksum of {code} is incorrect') 
    for code in incorrect_examples :
        checksum_number = checksum(code)
        if(checksum_number >= 0):
            print(f'The checksum of {code} is {checksum_number}')
        else: 
            print (f'The checksum of {code} is incorrect')              
    

if __name__ == "__main__":
    main()