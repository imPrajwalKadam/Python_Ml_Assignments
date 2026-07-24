"""
Write a python program that copies all .txt files from one directory to another every 10 minutes

- The Program should accept source and destination  directory
- Validate Both Directories
- copy only .txt file
- maintain log of copied files
- Avoid terminating if one file cannote be coppied

"""


import os 
import time
import schedule
import shutil
import sys


def FileCpyDirX(sourceDir,DestDir):
    timeStamp = time.ctime()


    

    if not os.path.exists(sourceDir):
        print("Automation Error : There is no such directory with name",sourceDir)
        return

    
    if not os.path.exists(DestDir):
        print("Automation Error : There is no such directory with name",DestDir)
        return

    if not os.path.isdir(DestDir):
            print("Automation Error : It is not a directory with name ",DestDir)
            return
    if not os.path.isdir(sourceDir):
            print("Automation Error : It is not a directory with name ",sourceDir)
            return
    

    for fileName in os.listdir(sourceDir):
         
        sourcePath = os.path.join(sourceDir,fileName)
        destPath = os.path.join(DestDir,fileName)

        if os.path.isfile(sourcePath):
              shutil.copy2(sourcePath,destPath)
        print("File Name : ",fileName)
        
         
def main():
    sourceDir = sys.argv[1]
    DestDir = sys.argv[2]

    schedule.every(10).minutes.do(FileCpyDirX,sourceDir,DestDir)

    print("Automation Script")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
