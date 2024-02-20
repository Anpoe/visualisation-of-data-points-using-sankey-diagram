#!/usr/bin/env python3
"""
Program name: clean_codes.py
Student number: 20021899

Clean manufacturers' codes, extracting numerical codes.
"""

def clean_code(code):
    """Remove manufacturers' extra information from the list, leaving only the numerical code.

    Args:
        code (string): String to be cleaned.
    Returns:
        Tuple (string, int): Numerical code extracted in string and integer formats.    
    """
    # Insert your code here (delete proxy code - return ("",0))    

    # set an empty str for new variable "sum"
    sum = ""
    # Iterate over every character in the string
    for i in code:
        # Determine if it is a digit
        if i.isdigit():
            # Add all characters together
            sum = sum + i
    # Turning strings into integers
    sum_number = int(sum)
    return sum, sum_number         
    

def main():
    code1 = "FlowFlex 4783569-B/N:305-S:67-CS1"
    result = clean_code (code1)
    print("Numeric code extracted: ", result [0])
    
    
if __name__ == "__main__":
    main()