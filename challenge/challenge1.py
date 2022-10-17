#!/usr/bin/env python3

def main():

    # input incurs a prompt on CLI for user type in information to be used in string.
    user_input = input("Please tell me your name: ")
    user_day = input("Could you tell me which day of the week it is? ")
    # f'string syntax, allows for direct input of variables into string without need of concatenation
    print(f"Hello, {user_input}! Happy {user_day}!")
    
main()
