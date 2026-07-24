"""
Write a python program that performs  file backup every hour.
The program should:
1. Accept the source file path .
2  Accept the destination file path.
3. copy the source file to the destination  directory .
4. Add the current date and time to the backup file name.
5. write the backup  operation details into.
backup_log.txt
Example backup file name
data_25_07_2026_16_30_00.txt
Example log entry:

Backup completed successfully at 25-07-2026 4:30:00 PM
use the shutil module for file copying.
"""
import shutil
import time
import datetime
import schedule 
import sys
import os



def isExists(filePath):
    if os.path.exists(filePath):
        return True
    else:
        return False

    
def fileXCpyBkp(FilePath,bkpFilePathDir):
    fileName =f"date_{datetime.datetime.now().strftime("%d-%m-%Y : %I:%M %p")}.txt" 

    shutil.copy(FilePath,bkpFilePathDir+f"/{fileName}")

    print(f"File Backup successfully at {datetime.datetime.now().strftime("%d-%m-%Y : %I:%M %p")}")

def main():

    sourceFilePath = sys.argv[1]


    DestFilePath = sys.argv[2]
    
    schedule.every(60).minutes.do(fileXCpyBkp,sourceFilePath,DestFilePath)

    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__ == "__main__":
    main()