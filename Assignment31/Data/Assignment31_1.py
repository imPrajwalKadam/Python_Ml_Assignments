"""
Write a program that accepts :
- A Message from the user
- A Time interval in seconds

Schedule the program to display the message repeatedly after the specified interval.

Example Input :
Enter Message : Jay Ganesh
Enter intervel in seconds: 5

Expected Output : Jay Ganesh 
                Every five seconds

Validate that the interval is greater than zero
"""
import time,schedule

def Display(msg):
    print(msg)

def main():

    msg = str(input("Enter a message : "))

    interVel = str(input("Enter intervel in seconds : "))

    schedule.every(int(interVel)).seconds.do(Display,msg)
    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__ == "__main__":
    main()