import sys
import os
import hashlib
from  pathlib import Path
import time
import datetime
import schedule
import smtplib
from email.message import EmailMessage
def calculatechkSum(fileName):
    fobj = open(fileName,"rb")

    hobj = hashlib.md5()
    Buffer  = fobj.read(1024)#1 byte
    
    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer  = fobj.read(1024)

    fobj.close()
    return hobj.hexdigest()


def findDeuplicate(dirName):
    ret = False
    ret = os.path.exists(dirName)

    if ret == False:
        print("Path is invalid ")
        return

    ret = os.path.isdir(dirName)

    if ret == False:
        print("it is not a directory")
        return

    duplicate = {}


    for folderName, subFolderName, fileName in os.walk(dirName):

        for fName in fileName:
            fName = os.path.join(folderName,fName)
            chkSum = calculatechkSum(fName)
            if chkSum in duplicate:
                duplicate[chkSum].append(fName)

            else:
                duplicate[chkSum] = [fName]

    return duplicate

def send_mail(sender,app_password,receiver,subject,body):
    #step 1: Create email object
    msg = EmailMessage()

    #step 2: set email headers
    msg["From"] = sender
    msg["to"] = receiver
    msg["subject"] = subject


    #step 3 : add mail body
    msg.set_content(body)

    #step 4 : create SMTP SSL connection manually 
    smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)

    # step 5 : Login using gmail + app password
    smtp.login(sender,app_password)

    # step 6 : send the email
    smtp.send_message(msg)

    #step 7: Close connection manully

    smtp.quit()



def deleteDuplicate(directoryName,emailAddress):
    scanningStartTime  = datetime.datetime.now().strftime("%H:%M:%S")

    Path("Marvellous").mkdir(exist_ok=True) #  exist_ok=True prevent program from crashing if folder is already exists 
    timeStamp = time.ctime()
    fileName = f"DuplicateRemovelLog_{timeStamp}.log"
    fileName = fileName.replace(" ","_")
    fileName= fileName.replace("-","_")

    border = "-"*80
    fobj = open("Marvellous/"+fileName,"a")
    
    myDict = findDeuplicate(directoryName)
    result = list(filter(lambda x: len(x) > 1 , myDict.values()))
    count = 0
    total = 0
    totalDeleted = 0
    totalScanned = 0
    deletedFielPath = ""
    deletedfileChecksum = ""
    for value in result:
        for subValue in value:
            totalScanned +=1
            count += 1

            if count > 1:
                print(subValue)
                checkSum = calculatechkSum(subValue)
                deletedfileChecksum += '\n'+ checkSum + "\n"
                deletedFielPath += '\n'+ subValue + '\n'
                os.remove(subValue)
                totalDeleted += 1

        count = 0



    scanningCompletionTime  = datetime.datetime.now().strftime("%H:%M:%S")
    print("Total deleted files :",totalDeleted)
   
    fobj.write(border+"\n\n")
    fobj.write(f"Starting time of dircetory scanning : {scanningStartTime} \n")
    fobj.write(f"Complition time of directory scanning : {scanningCompletionTime} \n")
    fobj.write(f"Scanned directory name : {directoryName}   \n")
    fobj.write(f"Total number of  files Scanned  : {totalScanned} \n")
    fobj.write(f"Total number of  duplicate file found  : {totalDeleted}   \n")
    fobj.write(f"Total number of  duplicate file deleted  : {totalDeleted}   \n")

    fobj.write(f"complite path of all deleted duplicate files  : {deletedFielPath}   \n")
    fobj.write(f"checksum vlues of deleted  files  : {deletedfileChecksum}   \n\n")
    fobj.write(border+"\n")

    border = "=" * 60
    subject = "Test mail from Python script"

    body = f"""Jay Ganesh,
                The Duplicate File removel  operation has been complited  successfully.
                Operation Statistics: 

                {border}

                Directory Scanning Report

                Starting Time                 : {scanningStartTime}
                Completion Time               : {scanningCompletionTime}
                Scanned Directory             : {directoryName}
                Total Files Scanned           : {totalScanned}
                Duplicate Files Found         : {totalDeleted}
                Duplicate Files Deleted       : {totalDeleted}

                Deleted File Paths:
                {deletedFielPath}

                Checksums of Deleted Files:
                {deletedfileChecksum}

                {border}
            """
    app_password = "lzzp kssk utju nfrb"
    sender_email = "prajwalsmtptesting03@gmail.com"

    send_mail(sender_email,app_password,emailAddress,subject,body)

def main():
    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
                print("Duplicate File Removel Automation")
                print("This script scans a directory, identifies duplicate files using checksums, ")
                print("Delete duplicate files ,create a log files, and sends a log files thorugh a mail .")


        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Python DuplicatefileRemovel.py <DirectoryName> <IntervelInMinutes> <ReceiverEmail>")
            print("Example DuplicatefileRemovel.py Demo 50 atharvak3.2000@gmail.com")
            print("DirectoryName should be absolute path")

    
    elif(len(sys.argv) == 4):
        
        absPath = sys.argv[1]
        timeInterval = sys.argv[2]
        emailAddress = sys.argv[3]

        schedule.every(int(timeInterval)).minutes.do(deleteDuplicate,absPath,emailAddress)
        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        print("Invalid number of argumets")

       
if __name__ == "__main__":
    main()