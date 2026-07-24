"""
Write a script that schedules the following tasks.
- Print Lunch time ! Every day at 1 pm .
- print wrape up work every day at 6pm

Both task should be handeled by seperate functions.

"""
import time 
import schedule
import datetime


def LunchTime():
      print("Lunch Time !")

def wrapeWork():
      print("Wrape up Work")
        
def main():
        schedule.every().day.at("23:42").do(LunchTime)
        schedule.every().day.at("23:43").do(wrapeWork)
        while True:
              schedule.run_pending()
              time.sleep(1)
        


if __name__ == "__main__":
    main()