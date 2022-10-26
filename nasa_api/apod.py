#!/usr/bin/python3

""" DOCSTRING """

import urllib.request
import requests
import json

NASA_API = "https://api.nasa.gov/planetary/apod?"

# def return_credits():
#    """ Obtains credentials from external file, modularization (micro-service) """
#    with open("/home/student/mycode/nasa_api/nasa.creds", "r") as nasa_creds:
#        cred = nasa_creds.read()

#    cred = "api_key=" + cred.strip("\n")
#    return cred

def main():
    """ Querying API """
    with open("/home/student/nasa.creds") as mycreds:
        nasacreds = mycreds.read()
    
    # Removes any extra lines that may be in our key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    
    # API call with key
    apodurlobj = urllib.request.urlopen(NASA_API + nasacreds)
    
    # read the given object
    apodread = apodurlobj.read()

    # decode object into Pythonic JSON
    apod = json.loads(apodread.decode("utf-8"))

    # show data from object
    print("\n\nConverted Pyton Data")
    print(apod)

    print()

    print(apod["title"] + "\n")

    print(apod["date"] + "\n")

    print(apod["explanation"] + "\n")

    print(apod["url"])

if __name__ == "__main__":
    main()
