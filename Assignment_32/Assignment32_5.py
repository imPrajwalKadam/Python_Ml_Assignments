"""
Write a program that delete all empty files from a specified directory every hour.

The Program should:
- Scan the directory recorsively
- Detect file whose size is zero bytes
- delete empty file
- Store deleted file paths in a log file
- handel permission error

Test the program only on a sample directory

"""


import os 
import time
import schedule
import sys


def FileDeleteDirX(dirName):
    timeStamp = time.ctime()
    if not os.path.exists(dirName):
        print("Automation Error : There is no such directory with name",dirName)
        return
    LogFileName = "deletedPath.log"



    if not os.path.isdir(dirName):
            print("Automation Error : It is not a directory with name ",dirName)
            return
    fobj = open(LogFileName,"a")
    border = 50 *"-"
    fobj.write(border +"\n\n")
    for DirName, subDirName,fileName in os.walk(dirName):
        for fName in fileName:
            if os.path.exists(fName):
                print("fName : ",fName, "File Size : ",os.path.getsize(fName))
                if os.path.getsize(fName) == 0:
                    os.remove(fName)      
                    fobj.write(f"{os.path.abspath(fName)} \n\n")

def main():
    Dir = sys.argv[1]

    schedule.every(5).seconds.do(FileDeleteDirX,Dir)

    print("Automation Script")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
