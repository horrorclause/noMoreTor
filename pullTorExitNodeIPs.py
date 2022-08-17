#!/usr/bin/env python3

from datetime import date
from checkIP import ipCheck
import wget

#TODO: Add date to naming convention for for downloaded torbulkexitlist 
# Downloads the latest Tor Bulk Exit List
def getTorList():
    siteUrl = "https://check.torproject.org/torbulkexitlist"
    bulkList = wget.download(siteUrl)

# Opens the "torbulkexitlist" file that was created from getTorList()
f = open("torbulkexitlist", "r")

#TODO: Add functionality to check daily API usage and use that as count
count = 1

# Checks if IPs from torbulkexitlist are identified as such in ABUSEIPDB
for ip in f.readlines():
    if count <= 10:
        checkedIP = ipCheck(ip.strip())
        if checkedIP != None:
            print(f"IP: {ip.strip()} -- Hostname: {checkedIP}")
        else:
            print(f"IP: {ip.strip()} requires further checking, does not have 'TOR' in hostname.")
        count+=1


#TODO: Add functionality to check if IPs are still associated with Tor, if not, remove them