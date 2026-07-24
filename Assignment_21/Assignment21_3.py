"""
Design a python application where multiple threads update a shared memory .
- Use lock to avoid a race conditions.
- Ech thread should increment the shared counter multiple times.
- Display the final value of the counter after all threads completes executation.   
"""

import threading
shared_counter = 0
counterLock = threading.Lock()


def thread1(no):
    global shared_counter
    for i in range(no):
        with counterLock:

            print("1st thread i :",i)
            shared_counter +=1
    print(f"Thread one output : {shared_counter}")


def thread2(no):
    global shared_counter
    for i in range(no):
        with counterLock:
            print("2nd thread i :",i)
            shared_counter +=1
    print(f"Thread two output : {shared_counter}")
        

def main():
    t1 = threading.Thread(target=thread1,args=(5,))
    t2 = threading.Thread(target=thread2,args=(10,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
if __name__ == "__main__":
    main()