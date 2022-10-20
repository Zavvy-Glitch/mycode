#!/usr/bin/python3

""" TLG Cohort D23 | CChea
    Parsing Log Files """

def main():
    
    #designated variables to count for loggin attempts
    loginfail = 0
    successful = 0
    
    #This line will open a specified file for reading. "r" in code signifies read.
    with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as readFile:

        #for loop to iterate over the file
        for line in readFile:

            #when one of the conditions is recognized below...(reading lines in keystone_file)
            if "- - - - -] Authorization failed" in line: #considered a conditional statement
                loginfail += 1 #if the condition in the above line is met it will add 1 to the loginfail variable
                print(line.split(" ")[-1])

            elif "-] Authorization failed" in line: #considered a conditional statement
                successful += 1 #if the condition in the line above is met it will add 1 to the successful variable

    print("The number of failed log in attempts is", loginfail)
    print("The number of successful login attempts is", successful)

main()
