#!/usr/bin/env python3

"""
Checks AbuseIPDB for verification of Tor Exit Nodes
"""

import requests
import json

def ipCheck(ip):
    # Defining the api-endpoint
    url = 'https://api.abuseipdb.com/api/v2/check'

    # Test with known Tor IP
    queryString = {
        'ipAddress': ip
    }

    # Key is personal API key
    headers = {
        'Accept': 'application/json',
        'Key': "3eb37206ccfb88da19a801be0e31964ac7d072817efba30d6e544a206a81ff54cee6dd1880e4b783"
    }

    response = requests.request(method='GET', url=url, headers=headers, params=queryString)

    # Information is returned as a dictionary with a single key = 'data' and value of another dictionary
    ipDict = json.loads(response.text)

    # iterating through data to see if "tor" is listed, if it is return the hostname, else returns "None"
    for x in ipDict['data'].items():
        try:
            for entry in x:
                if entry == "hostnames":
                    if "tor" in x[1][0]:

                        return x[1][0]
        except IndexError as e:
            # List index out of range, no hostname provided
            #print(ip,x, e)
            return None


"""f = open("torBulkExitList-2022-08-17.txt", "r")

for i in f.readlines():
    print(ipCheck(i.strip()))
#print(ipCheck("109.70.100.8"))"""