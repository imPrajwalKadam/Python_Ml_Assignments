"""
Design a python application that creates two seperate threads named even and odd
The even thread shuld display the first 10 even number
the Odd thread should display the first 10 odd numbers 
both threads should executes independently using the threading module
insure proper thread creation and execution
"""
import threading
import time

def evenThread(no):
    for i in range(2,no,2):
        print(i,end=" ")
    print()

def oddThread(no):
    for i in range(1,no,2):
        print(i,end=" ")
    print()

def main():
    start_time = time.perf_counter()

    t1 = threading.Thread(target=evenThread,args=(10,))

    t2 = threading.Thread(target=oddThread,args=(10,))

    t1.start()
    print("-"*50)
    t2.start()
    t1.join()
    t2.join()   
    end_time = time.perf_counter()
    print(f"Time required is :{end_time - start_time:.4f} seconds ")

if __name__ == "__main__":
    main()