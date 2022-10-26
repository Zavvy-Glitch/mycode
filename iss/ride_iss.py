#!/usr/bin/python3

""" TLG Cohort D23 | CChea
    Astronauts on ISS """

import urllib.request
import json

MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    """ Used to read JSON object from API MAJORTOM """
    
    # API Call made here
    groundctrl = urllib.request.urlopen(MAJORTOM)
    
    # strips the attachment (JSON)
    # this will be read out as a string
    helmet = groundctrl.read()

    # print data as is
    print(helmet)

    # this converts the data to usable list / dict
    helmetson = json.loads(helmet.decode("utf-8"))

    # print the data types
    # bytes
    print(type(helmet))

    #dict
    print(type(helmetson))

    print(helmetson["number"])

    # return a LIST of people on the ISS
    print(helmetson["people"])

    # returns the first astronaut in the list
    print(helmetson["people"][0])

    # list the SECOND astro in the list
    print(helmetson["people"][1])

    # list the LAST astro in the list
    print(helmetson["people"][-1])

    # display every item in a list
    for astro in helmetson["people"]:
        # display what astro is
        print(astro)

    # display every item in a list
    for astro in helmetson["people"]:
        # display ONLY the name value associated with astro
        print(astro["name"])

if __name__ == "__main__":
    main()
