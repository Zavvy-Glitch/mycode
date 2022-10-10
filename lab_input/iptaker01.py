#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   print() - display data to std out"""

# below is a function containing our code
def main():

    # pause the program and wait for the user to provide input
    user_input = input("Please enter an IPv4 IP address:")
    
    # display the input back to the user.
    print("You told me the IPv4 address is: " + user_input)
    
    # ask user for 'vendor name'
    user_vendor = input("Please input the vendor name: ")
    print("The vendor is: " + user_vendor)
# this calls main
main()

