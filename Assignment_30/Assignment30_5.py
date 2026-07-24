"""
Schedule a task  that executes  every five minutes.
That task should write the current date and time a file named: Marvellous.txt

new entries  should be appended without removing previous entries.

Example file cotents:

Task executed at : 25-07-2026 04:30:00 pm
Task executed at : 25-07-2026 04:35:00 pm
Task executed at : 25-07-2026 04:40:00 pm

"""

import time 
import schedule
import datetime


def WriteFile():
        print(datetime.datetime.now().strftime("%d-%m-%Y : %I:%M %p"))
        border = 50*"-"

        fobj = open("Marvellous.txt","a")

        fobj.write(border+"\n")

        fobj.write(f"Task executed at : {datetime.datetime.now().strftime("%d-%m-%Y : %I:%M %p")} \n\n")
        fobj.write(border+"\n")

        fobj.close()

def main():
        schedule.every(5).seconds.do(WriteFile)
        print("Automation Script")

        while(True):
               schedule.run_pending()
               time.sleep(1)
            




if __name__ == "__main__":
    main()