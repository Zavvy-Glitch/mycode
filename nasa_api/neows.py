#!/usr/bin/python3

""" DOCSTRING """

import requests

NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

def return_creds():
    with open("/home/student/nasa.creds", "r") as my_creds:
        nasa_creds = my_creds.read()

    nasa_creds = "api_key=" + nasa_creds.strip("\n")
    return nasa_creds

def main():
    nasa_creds = return_creds()

    start_date = "start_date=2022-10-01"

    neow_request = requests.get(NEOURL + start_date + "&" + nasa_creds)

    neow_data = neow_request.json()

    print(neow_data)

if __name__ == "__main__":
    main()
