#!/usr/bin/env python3


'''
moving to be deprecated - torCheck.py will be more optimized.


'''
from datetime import date
from checkIP import ipCheck
import wget

today = date.today()

vName = f"verifiedTorList-{today}.txt"  # Name for verified IP list
rName = f"needReviewTorList-{today}.txt"  # Name for IPs that need Review    


# Downloads the latest Tor Bulk Exit List
def getTorList():
    siteUrl = "https://check.torproject.org/torbulkexitlist"
    wget.download(siteUrl, f"torBulkExitList-{today}.txt")

getTorList()

#TODO: Create Master blocklist of confirmed IPs, and list of IPs that need to be verified

def createLists():

    #TODO: Add functionality to check if torBulkExitList is present for today's date, if not, create it first then proceed 

    # Opens the "torBulkExitList.txt" file that was created from getTorList()
    f = open(f"torBulkExitList-{today}.txt", "r")

    #TODO: Add functionality to check daily API usage and use that as count
    count = 1

    # Verified IP list and naming convention
    verifiedIPs = open(vName, "w")
    ipsNeedReview = open(rName, "w")

    reviewIPsList = set()

    # Checks if IPs from torbulkexitlist are identified as such in ABUSEIPDB
    for ip in f.readlines():
        if count <= 1000:
            checkedIP = ipCheck(ip.strip())
            if checkedIP != None:
                #print(f"IP: {ip.strip()} -- Hostname: {checkedIP}")
                # Adds verified IP to verifiedIP file
                verifiedIPs.write(ip)
                
            else:
                #print(f"IP: {ip.strip()} requires further checking, does not have 'TOR' in hostname.")
                reviewIPsList.add(ip.strip())
                ipsNeedReview.write(ip)
            count+=1


    f.close()
    verifiedIPs.close()
    ipsNeedReview.close()

    return reviewIPsList

#TODO: Add functionality to check if IPs are still associated with Tor, if not, remove them

print(f"{vName} was created.")
print("The following IPs need review:")
print(createLists())