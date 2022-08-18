#!/usr/bin/env python3

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

        todaysList = open(f"torBulkExitList-{today}.txt", "r")
        for x in todaysList.readlines():
            todayTor.add(x.strip())

        yesterdaysList = open(f"torBulkExitList-{yesterday}.txt", "r")
        for y in yesterdaysList.readlines():
            yesterdayTor.add(y.strip())

        #TODO: Add write to log file here +--------------------------+
        #new = [ip for ip in todayTor if ip not in yesterdayTor] # Checks if an ip is in today's list that is not in yesterday's
        logEntries = {
        "Date" : today,
        "IP Change" : [ip for ip in todayTor if ip not in yesterdayTor],
        }

        torLog = open("torLog.txt", "a")

        for k,v in logEntries.items():
            torLog.write(f"{k} : \n{v}")
        torLog.write("[+]---------------------------[+]\n")



        todaysList.close()
        yesterdaysList.close()
        torLog.close()

        return torLog
  
    except Exception as e:
        print(e)


print(getTorList())





