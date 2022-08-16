#!/usr/bin/env python3

"""
Checks AbuseIPDB for verification of Tor Exit Nodes
"""

import requests
import json

# Defining the api-endpoint
url = 'https://api.abuseipdb.com/api/v2/check'

# Test with known Tor IP
queryString = {
    'ipAddress': '2602:fd92:05e9:aeaf:0000:0000:0000:0001'
}

# Key is personal API key
headers = {
    'Accept': 'application/json',
    'Key': "3eb37206ccfb88da19a801be0e31964ac7d072817efba30d6e544a206a81ff54cee6dd1880e4b783"
}

response = requests.request(method='GET', url=url, headers=headers, params=queryString)

# Formatted output
decodedResponse = json.loads(response.text)

print(json.dumps(decodedResponse, sort_keys=True, indent=4))