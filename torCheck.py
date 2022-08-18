#!/usr/bin/env python3

from time import time
import wget
from os import path
from datetime import date, timedelta



def getTorList():

    today = date.today()
    yesterday = today - timedelta(days=1)

    try:
        if path.isfile(f"torBulkExitList-{today}.txt") is False:
            siteUrl = "https://check.torproject.org/torbulkexitlist"
            wget.download(siteUrl, f"torBulkExitList-{today}.txt")
            
            print(f"[+] torBulkExitList-{today}.txt has been created")

        else:
            print(f"[X] torBulkExitList-{today}.txt already exists")

        todayTor = set()
        yesterdayTor = set()

        for x in open(f"torBulkExitList-{today}.txt", "r").readlines():
            todayTor.add(x.strip())

        for y in open(f"torBulkExitList-{yesterday}.txt", "r").readlines():
            yesterdayTor.add(y.strip())

        new = [ip for ip in todayTor if ip not in yesterdayTor] # Checks if an ip is in today's list that is not in yesterday's
        
        return new
    
    except Exception as e:
        print(e)

print(getTorList())





