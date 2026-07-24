"""
Write a program that creates a new text file every minute.
The file should contain the current timestamp.

Example :
File_25_07_2026_16_30_00.txt

Write the following information into the file:

- file name
- creation date
- creation time
"""

import time
import schedule
import datetime


def createFile():
    timeStamp = time.ctime()
    print("time stamp is :",timeStamp)
    fileName = "File_%s.txt"%(timeStamp)
    fileName = fileName.replace(" ","_")
    fileName = fileName.replace(":","_")

    print("Log file created : ",fileName)
    fobj = open(fileName,"w")
    fobj.write(f"{timeStamp} \n")

    fobj.close()

def main():
    schedule.every(1).minute.do(createFile)
    print("Automation Script")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
