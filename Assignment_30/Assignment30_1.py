"""
Write a python program that prints :
Jay Ganesh...
every two times 

USE :
Schedule.every(2).seconds.do(...)

Expected output:
Jay Ganesh...
Jay Ganesh...
Jay Ganesh...
"""
import schedule
import time

def Display():
    print("Jay Ganesh...")

def main():
    print("Automation script...")
    schedule.every(2).seconds.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
