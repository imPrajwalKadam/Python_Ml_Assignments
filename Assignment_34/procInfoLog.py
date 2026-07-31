"""
Design automation script  which Accept directory name from user and create log file in that directory which contains 
 information of running processes as its name ,PID,Username.
    Usage : ProcInfoLog.py Demo

    Demo is name of directory

"""
from  processScanModule import process_scan
import smtplib
import time
import os
import sys
from email.message import EmailMessage
from pathlib import Path
import mimetypes


def send_mail(sender,app_password,receiver,subject,body,filePath):
    #step 1: Create email object
    msg = EmailMessage()

    #step 2: set email headers
    msg["From"] = sender
    msg["to"] = receiver
    msg["subject"] = subject


    #step 3 : add mail body
    msg.set_content(body)
    file_path = Path(filePath)
    # 3. Guess the file type automatically
    mime_type, _ = mimetypes.guess_type(file_path.name)
    if mime_type is None:
        # Default to generic binary stream if type is unknown
        mime_type = "application/octet-stream" 
    main_type, sub_type = mime_type.split("/", 1)


    # 4. Read the file and attach it
    with open(file_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype=main_type,
            subtype=sub_type,
            filename=file_path.name
        )

    #step 4 : create SMTP SSL connection manually 
    smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)

    # step 5 : Login using gmail + app password
    smtp.login(sender,app_password)

    # step 6 : send the email
    smtp.send_message(msg)

    #step 7: Close connection manully

    smtp.quit()


def runningProcessInfo(folderName,emailId):
    ret = False
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
    for info in data:
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
    fobj.flush()  # Forces data out of buffer onto disk
    fobj.close()  # Closes the file safely

    print(f"{border + border}")
    subject = "Information of running processes"

    body = f"""Jay Ganesh,
                check Attach file which contains information about running process
            """
    app_password = "lzzp kssk utju nfrb"
    sender_email = "prajwalsmtptesting03@gmail.com"

    send_mail(sender_email,app_password,emailId,subject,body,filename) 
    print("mail sent successfully")

def main():
    if len(sys.argv) == 3:
        runningProcessInfo(sys.argv[1],sys.argv[2])
if __name__ == "__main__":
    main()