"""
Design automation script  which display information of running processes as its name ,PID,Username.
    Usage : ProcInfo.py

"""
from  processScanModule import process_scan
import time
import os
import sys

def ProcessInfo():
    ret = False
    folderName = "procInfo"
    ret = os.path.exists(folderName)
    if ret == True:
        ret = os.path.isdir(folderName)
        if ret == False:
            print("Unable to process directory it exists but it not a directory...")
            return
    else:
        os.mkdir(folderName)
        print("directory for procInfo gets created ...")


    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    border = 50*"-"

    filename = os.path.join(folderName,"All_procInfo_log_%s.log" %timestamp)

    fobj = open(filename,"w")
    print(f"log file gets created with name {filename}")

    data = process_scan()
    fobj.write(f"{border + border}\n")
    fobj.write("---------------------------------Information of All Process ---------------------------------------------\n")
    for info in data:
        print(border)
        print(f"Process ID : {info.get("pid")}\n")
        print(f"Process Name : {info.get("name")}\n")
        print(f"Process UserName : {info.get("username")}\n")
        print(f"Process Status : {info.get("status")}\n")

        fobj.write(f"{border} \n")
        fobj.write(f"Process ID : {info.get("pid")}\n")
        fobj.write(f"Process Name : {info.get("name")}\n")
        fobj.write(f"Process UserName : {info.get("username")}\n")

    fobj.write(f"{border + border}")
    print(border)


"""
Task 2 Design Automation script which accept process name and display information of that process 
if it is running 
Usage = procInfo.py NotePad
"""
def runningProcessInfo(processName):
    ret = False
    folderName = "procInfo"
    ret = os.path.exists(folderName)
    if ret == True:
        ret = os.path.isdir(folderName)
        if ret == False:
            print("Unable to process directory it exists but it not a directory...")
            return
    else:
        os.mkdir(folderName)
        print("directory for procInfo gets created ...")


    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    border = 50*"-"

    filename = os.path.join(folderName,"Running_procInfo_log_%s.log" %timestamp)

    fobj = open(filename,"w")
    print(f"log file gets created with name {filename}")
    
    data = process_scan()
    border = "-"*50
    
    fobj.write(f"{border + border} \n")
    fobj.write("--------------------------------Information Of Running Process----------------------------------------- \n")
    print(processName)
    for info in data:
        print(info.get("name"))
        if info.get('name') == processName:
            if info.get('status') == "running":
                print(border)
                print(f"Process ID : {info.get("pid")}\n")
                print(f"Process Name : {info.get("name")}\n")
                print(f"Process UserName : {info.get("username")}\n")
                print(f"Process Status : {info.get("status")}\n")
                fobj.write(f"{border} \n")
                fobj.write(f"Process ID : {info.get("pid")}\n")
                fobj.write(f"Process Name : {info.get("name")}\n")
                fobj.write(f"Process UserName : {info.get("username")}\n")
            

    fobj.write(f"{border+border}")
    print(border)

def main():
    if len(sys.argv) == 2:
        runningProcessInfo(sys.argv[1])
    else:
        ProcessInfo()

if __name__ == "__main__":
    main()