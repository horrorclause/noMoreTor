#!/usr/bin/env python3

from datetime import date
from checkIP import ipCheck
import wget

today = date.today()
print(today)

#TODO: Add date to naming convention for for downloaded torbulkexitlist 
# Downloads the latest Tor Bulk Exit List
def getTorList():
    siteUrl = "https://check.torproject.org/torbulkexitlist"
    bulkList = wget.download(siteUrl)

#TODO: Create Master blocklist of confirmed IPs, and list of IPs that need to be verified

# Opens the "torbulkexitlist" file that was created from getTorList()
f = open("torbulkexitlist", "r")

#TODO: Add functionality to check daily API usage and use that as count
count = 1

# Verified IP list and naming convention
vName = f"verifiedTorList-{today}.txt"
verifiedIPs = open(vName, "w")

# Checks if IPs from torbulkexitlist are identified as such in ABUSEIPDB
for ip in f.readlines():
    if count <= 10:
        checkedIP = ipCheck(ip.strip())
        if checkedIP != None:
            print(f"IP: {ip.strip()} -- Hostname: {checkedIP}")
            # Adds verified IP to verifiedIP file
            verifiedIPs.write(ip)
            print(f"Added {ip.strip()} to {vName}\n")
        else:
            print(f"IP: {ip.strip()} requires further checking, does not have 'TOR' in hostname.")
        count+=1


f.close()
verifiedIPs.close()

#TODO: Add functionality to check if IPs are still associated with Tor, if not, remove them