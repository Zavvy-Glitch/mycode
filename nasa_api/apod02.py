#!/usr/bin/python3

""" TLG Cohort D23 | CChea
    API Querying & Slicing Data """

import requests

NASA_API = "https://api.nasa.gov/planetary/apod?"

def return_creds():
    with open("/home/student/nasa.creds", "r") as my_creds:
        nasa_creds = my_creds.read()

        nasa_creds = "api_key=" + nasa_creds.strip("\n")
        return nasa_creds

def main():
    nasa_creds = return_creds()

    apod_res = requests.get(NASA_API + nasa_creds)

    apod = apod_res.json()

    print(apod)

    print()

    print(apod["title"] + "\n")

    print(apod["date"] + "\n")

    print(apod["explanation"])

    print(apod["url"])

if __name__ == "__main__":
    main()
