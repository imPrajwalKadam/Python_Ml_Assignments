"""
Write a python program that monitors the size of specified file every 30 seconds 

Write the following details  into:
FileSizeLog.txt
- File path
- File size in bytes
- date and time
Handel the sitiuation where the the file does not exist
"""

import time
import schedule
import datetime
import os



def MonitorFile():
    timeStamp = time.ctime()

    ret = os.path.exists("FileSizeLog.txt")

    if ret == False:
        print("File Does Not Exists")

    print("time stamp is :",timeStamp)

    fobj = open("FileSizeLog.txt","a")
    border = 50 *"-"

    fobj.write(border+"\n\n")
    fobj.write(f"File Path : {os.path.abspath("demo.txt")}\n")
    fobj.write(f"File size in bytes : {os.path.getsize("demo.txt")}\n")
    fobj.write(f"{timeStamp} \n\n")

    fobj.write(border)

    fobj.close()

def main():
    schedule.every(30).seconds.do(MonitorFile)
    print("Automation Script")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
