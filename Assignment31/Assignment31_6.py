"""
Write a program that schedules the following messages:
- Monday at 9:00 AM : Start Your weekly goals
- Widnesday at 5:00 PM : Review your weekly progress
- friday at 6:00 PM : Weekly work complited

USE :

schedule .every().monday.at(..)
schedule .every().widnesday.at(..)
schedule .every().friday.at(..)


"""

import schedule
import time
import datetime
import os


def ModayTask():
    print("Start Your Weekly goals")

def WidnesDayTask():
    print("Review Your weekly progress")

def fridayTask():
    print("Weekly Work complited")

def main():
    schedule .every().monday.at("09:00").do(ModayTask)
    schedule .every().wednesday.at("17:00").do(WidnesDayTask)
    schedule .every().friday.at("18:00").do(fridayTask)
    
    print("Automation script started...")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()