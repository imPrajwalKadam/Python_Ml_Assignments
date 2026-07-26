"""
Write a python program that creates a new log file after every 10 minutes .
Example :
MarvellousLog_25_07_2026_16_30_00.txt
The File should contain :
Log file created cuccesfully
Creation time: 25-07-2026 4:30:00 PM
"""

import os 
import schedule
import datetime
import time
def CreateFile():
    print("Log File Created successfully ")
    fileName = f"MarvellousLog_{time.ctime()}"
    fobj = open(fileName,"a")
    fobj.write(f"Creation time : {datetime.datetime.now()} \n")

def main():

    print("Automation script ")
    schedule.every(10).minutes.do(CreateFile)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()