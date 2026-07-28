import psutil
import sys
import os
import time
import schedule


def processScan():
    listProcess = []

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["pid","name","username","status"])
        info["cpu_percent"] = proc.cpu_percent(None)
        info["memory_percent"] =proc.memory_percent()
        listProcess.append(info)

    return listProcess    

        
def platformSurrvillence(folderName):
    border = "-"*50
    ret = False
    ret = os.path.exists(folderName)

    if (ret == True):
        ret = os.path.isdir(folderName)
        if (ret == False):
            print("unable to process directry it exist  but its not a directory")
            return

    else:
        os.mkdir(folderName)
        print("Directory for the log file gets created successfully")

    timeStamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    fileName = os.path.join(folderName,"Marvellous_%s.log" %timeStamp)
    fobj = open(fileName,"w")
    
    print(f"log file gets successfully created with name {fileName}")

    fobj.write(border+"\n")
    fobj.write("-----Marvellous Patform Surrvillance System -----\n")

    fobj.write("Lof file gets created at : " + timeStamp + "\n")

    fobj.write(border+"\n\n")
    fobj.write("-------------------System Report ---------------------\n")

    #CPU Information
    fobj.write("Number of active cpu cores : %s %%\n" %psutil.cpu_count())
    fobj.write("CPU Usage: %s \n" %psutil.cpu_percent())
    fobj.write(border+"\n")


    #RAM Information
    memory = psutil.virtual_memory()

    fobj.write("RAM Usage: %s %%\n" %memory.percent)

    fobj.write("Total RAM Available : %s \n" %memory.total)

    fobj.write(border+"\n")

    #Disk Usage of all Partition
    fobj.write("Disk Usage of all partition \n")
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            fobj.write("%s -> %s %% used \n"%(part.mountpoint,usage.percent))
        except:
            pass
    fobj.write(border+"\n")

    #Network Usage report
    netObj = psutil.net_io_counters()

    fobj.write("Network Usage report \n")
    fobj.write("Send : %.2f MB\n"%(netObj.bytes_sent / 1024 * 1024))
    fobj.write("Recive : %.2f MB\n"%(netObj.bytes_recv / 1024 * 1024))

    fobj.write("\n"+border+"\n")


    #Process Log
    data = processScan()
    for info in data:
        fobj.write(f"{info} \n")
        fobj.write("pId : %s\n"%info.get("pid"))
        fobj.write("Name : %s\n"%info.get("name"))
        fobj.write("username : %s\n"%info.get("username"))
        fobj.write("user name : %s\n"%info.get("username"))
        fobj.write("Status : %s\n"%info.get("status"))
        fobj.write("CPU Usage : %.2f \n"%info.get("cpu_percent"))
        fobj.write("RAM Usage : %.2f \n"%info.get("memory_percent"))
        fobj.write(border+"\n")


    fobj.write(border+"\n")
    fobj.write("---------------- End Of Log File --------------------\n")
    fobj.write(border+"\n")

    fobj.close()

def main():
    border = "-"*50
    print(border)
    print("-----Marvellous Paltform Surrvillance System -----")

    #--h and --u handling
    if len(sys.argv) == 2:
        if (sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("this automation script is used to performed ")

            print("1 : It Fetch the information of running processes")
            print("2 : It fetch information about promery storage as RAM")
            print("3 : It Fetch information about the secondery strage as HDD")
            print("4 : It Fetch information about the microprocessor")
            print("4 : It gets auto schedule periodically ")
            print("6 : It maintaince records into log file")
            print("7 : It send log files through mail periodically")

        elif (sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as : ")
            print(f"Python {sys.argv[0]} : time_interval folder_name")
            print("Time_intervels : Time in minutes for peridic execution")
            print("Filder_name : Name of folder of log file creation")
            
        else:
            print("Unable to proceeed as there is no matching argument")
            print("Please use --h  or --u fpr getting more details")


    #actual project code
    elif len(sys.argv) == 3:
        # print("CPU Usage : ",psutil.cpu_percent())
        print("Scheduler started successfully")
        print("Press ctrl+c to abort the automation script")
        schedule.every(int(sys.argv[1])).seconds.do(platformSurrvillence,sys.argv[2])
        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        print("Invalid number of aruments")
        print("Unable to proceed as  argument not matching ")
        print("Please use --h  or --u fpr getting more details")

    print(border)

    print("--- Thank You for using our automation system --- ")
    print(border)




if __name__ == "__main__":
    main()