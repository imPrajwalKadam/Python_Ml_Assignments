"""
Write a program that scans a specified directory  every minute.
- The Task should Display.
- Number of files
- Number of subdirectory
- Date and time of scanning
use the os module .
Example output :
    Directory Scanned: E:/Data
    Total Files: 15
    Total subdirectories : 4
    Scan Time 25-07-2026 4:30:00 PM 
"""
import os
import sys

def DirScanner(DirPath):
    print(DirPath)
    fileCnt = 0
    totalSubDirCnt = 0
    for folderName, subFolderName,FileName in os.walk(DirPath):
        for file in FileName:
            fileCnt += 1
        for subFldrNme in subFolderName:
            totalSubDirCnt+=1
    print("Directory Scanned : ",os.path.abspath(DirPath))
    print("Total Files : ",fileCnt)
    print("Total Subdirectories ",totalSubDirCnt)


def main():
     dirName = sys.argv[1]
     DirScanner(dirName)


if __name__ == "__main__":
    main()
