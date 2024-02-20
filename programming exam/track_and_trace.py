#!/usr/bin/env python3
'''
Program name: track_and_trace.py
Student number: 20021899

The user will answer the questions from the flowchart, receiving the required information.
'''

def main():
    # Delete the pass statement and insert your code here.
    """ question and answer processor
    paramaters:
        yes: list
            accepted answer for "yes" statement
        no:  list
            accepted answer for "no" statement

    return:
        False
    """

    yes = ['Y','y','Yes','yes','YES','YeS',"yEs",'yeS',"yES"]
    no = ['N','n','No',"no",'nO','NO']

    # while loop, if return False then stop.
    while True:
        # print question asked
        print("\nDo you have symptoms?")
        # input request
        ans1 = input(" \nType your answer here(Yes/No): ")
        # determine whether ans is in list yes
        if ans1 in yes:
            print("\nSelf-isolate immediately and book a test.")
            print("\nTested positive for coronavirus?")
            ans2 = input(" \nType your answer here(Yes/No): ")
            if ans2 in yes:
                print("\nSelf isolate for 10 day from date of  first symptoms or of test, \
                    whichever is earliest.")
                # Out of the loop
                return False
            # determine whether ans is in list no
            elif ans2 in no:
                print("\nReturn to work if you are well enough to do so.")
                # Out of the loop
                return False
            else:
                print("\nInvalid answer, please use yes/no to answer.")
        # determine whether ans is in list no
        elif ans1 in no:
            print("\nHave you been told by NHS Test&Trace that you're a close \
                contact of an infected person?")
            ans3 = input(" \nType your answer here(Yes/No): ")
            # determine whether ans is in list yes
            if ans3 in yes:
                print("\nSelf-isolate for 10 days. Work from home if you can. You will receive full pay, \
                    but will need evidence of your contact with the NHS.")
                # Out of the loop
                return False
            # determine whether ans is in list no
            elif ans3 in no: 
                print("\nAttend Work.")
                # Out of the loop
                return False
            # if input is not in list yes or list no
            else:
                print("\nInvalid answer, please use yes/no to answer.")
        else:
            print("\nInvalid answer, please use yes/no to answer.")


if __name__ == "__main__":
    main()