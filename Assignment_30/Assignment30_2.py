"""
Write a python program that display current date time ater every one minute.

Use the datetime module 


Expected output:
Current date and time : 25-07-2026 04:30:00 PM
"""
import time
import datetime
import schedule

def DisplayDateTime():
    print("Current Date time : ",datetime.datetime.now() )

def main():
    schedule.every(1).second.do(DisplayDateTime)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
