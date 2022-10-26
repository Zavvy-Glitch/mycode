#!/usr/bin/python3

""" TLG Cohort D23 | CChea
    Tracking the ISS usin open API """

import requests

# Defines our pathway
MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
    """RUNTIME CODE"""

    # Make a service request
    groundctrl = requests.get(MAJORTOM)
    # send a post with requests.post()
    # send a put with requests.put()
    # send a delete with requests.delete()
    # send a head with requests.head()

    ## strip the json off the 200 that was returned by our API
    ## translate the json into python lists and dictionaries
    helmetson = groundctrl.json()

    # prints pythonic data
    print("\n\nConverted Python Data")
    print(helmetson)

    print('\n\nPeople in Space:', str(helmetson['number']))
    for astro in helmetson['people']:
        print('Astronaut:', astro["name"] + '\nAssigned Ship:', astro["craft"])

if __name__ == "__main__":
    main()
