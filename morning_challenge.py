#!/usr/bin/env python3

import requests
import time
import datetime
import reverse_geocoder as rg

"""Returning the location of the ISS in latitude/longitude"""

URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()
    #time = resp['timestamp']
    #date = datetime.datetime.fromtimestamp(time)
    lat = resp['iss_position']['latitude']
    lon = resp['iss_position']['longitude']
    ts = resp['timestamp']

    hr_ts = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ts))

    locator_resp = rg.search((lat, lon))

    city = locator_resp[0]['cc']

    print("""
CURRENT LOCATION OF THE ISS:
Timestamp: {hr_ts}
Lon: {lon}
Lat: {lat}
City/Country: {city}, {country}
""")


if __name__ == "__main__":
    main()

#lat= 28.613939
#lon= 77.209023

# reverse_geocoder MUST be passed a tuple as the argument!
#coords_tuple= (lat, lon)

#result = rg.search(coords_tuple)
