"""
Write a program that schedules a function that print:
Coding kar...!
every 30 minutes.
"""

import time 
import schedule


def Display():
    print("Coding kar...!")

def main():
    print("Automation script...")
    schedule.every(30).minutes.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__ == "__main__":
    main()