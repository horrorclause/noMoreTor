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

    # Formatted output
    #decodedResponse = json.loads(response.text)
    #json.dumps(decodedResponse, sort_keys=True, indent=4)

    # Information is returned as a dictionary with a single key = 'data' and value of another dictionary
    return json.loads(response.text)


"""
# iterating through data to see if "tor" is listed
for i in ipCheck('109.70.100.8')['data'].items():
    for x in i:
        if x == "hostnames":
            if "tor" in i[1][0]:
                print(i[1][0])
"""
