"""
Write a program that reads and displays the contents of a specified text file every minute.

Handel the following condition
- File does not exist 
- File is empty
- Permision is denied
- file cannot be opened

"""
import os 
import time
import schedule

import sys


def DisplayFileContent(fileName):
    timeStamp = time.ctime()


    # permission is denied
    ret = os.access(fileName,os.R_OK)
    if ret == False:
        print("Read Permission is denied")
        return

    ret = os.path.exists(fileName)

    #- File does not exist 
    if ret == False:
        print("File Does Not Exists")
        return

    # file is empty
    if os.path.getsize(fileName) <=0:
        print("File is empty")
        return


    fobj = open(fileName,"r")

    
    if fobj.closed:
        print("File Dies not opened")
        return
    border = 50 *"-"

    data = fobj.read()
    print(border+"\n\n")
    print(f"{data}\n\n")
    print(border)


    fobj.close()

def main():
    fName = sys.argv[1]
    schedule.every(3).seconds.do(DisplayFileContent,fName)
    print("Automation Script")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
