"""
Create a function named:
DisplayMessage(message)

schedule.every(5).seconds.do(displayDisplayMessage,message)
The message should be accepted from  the user .

"""

import time,schedule

def Display(msg):
    print(msg)

def main():

    msg = str(input("Enter a message : "))


    schedule.every(5).seconds.do(Display,msg)
    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__ == "__main__":
    main()