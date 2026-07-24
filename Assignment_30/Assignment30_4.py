"""
Create a task that executes every day at 9 am and print:
Namaskar..
usee:
schedule.every().day.at("9:00").do(....)
"""
import time
import schedule

def Display():
    print("Namaskar....")


def main():
    print("Automations script...")
    schedule.every().day.at("9:00").do(Display)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()