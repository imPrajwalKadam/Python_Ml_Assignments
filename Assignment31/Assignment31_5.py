"""
Write a program that accepts  a directory name from the user and count number of files inside it every five minutes

Write the result into 
DirectoryCountlog.txt 
Each entry should contain
-Directory path
- number of files   
- date and time
"""

import schedule
import time
import datetime
import os

def DirectoryCount(dirPath):
    fileCount = 0
    for folderName,subfolderName, fileName in os.walk(dirPath):
        for fName in fileName:
            fileCount += 1

    border = 50*"-"
    fobj = open("DirectoryCountLog.txt","a")
    fobj.write(f"{border} \n\n")
    fobj.write(f"Directory Path is : {os.path.abspath(dirPath)}\n")
    fobj.write(f"Number of files : {fileCount}  \n")
    fobj.write(f"{datetime.datetime.now()} \n\n")
    fobj.write(f"{border} ")

    print("Task Complited sucessfully")


def main():
    dirName = str(input("Enter directory name : "))
    schedule.every(5).minutes.do(DirectoryCount,dirName)

    print("Automation script started...")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()