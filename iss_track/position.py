#!/usr/bin/python3

""" TLG Cohort D23 | CChea
    Wittle down data from ISS API """

import reverse_geocoder as rg
import requests
import datetime

def main():
    """ Retrieving Data from ISS-NOW API """
    # API Call
    iss_data = requests.get('http://api.open-notify.org/iss-now.json').json()
    # print(iss_data)
    
    timestamp = iss_data['timestamp']
    latitude = iss_data['iss_position']['latitude']
    longitude = iss_data['iss_position']['longitude']

    date_time = datetime.datetime.fromtimestamp(timestamp)
    result = rg.search((latitude, longitude))
    # print(result) <--- helps to display data to understand which way to walk down the data
    
    city = result[0]['name']
    country = result[0]['cc']

    # print("CURRENT LOCATION OF THE ISS: \n", iss_data['iss_position']['latitude'] + iss_data['iss_position']['longitude'])

    print(f"""
    CURRENT LOCATION OF ISS:
    Time Stamp: {date_time}
    Longitude: {longitude}
    Latitude: {latitude}
    City/Country: {city}, {country}
    """)

if __name__ == "__main__":
    main()
