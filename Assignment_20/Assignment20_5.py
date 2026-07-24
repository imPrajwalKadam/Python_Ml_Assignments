"""
Design a python application that creates two threads named Thread1 and Thread2.

- Thread1 should display number from 1 to 50 

- Thread2 should display number from 50 to 1 in reverse order

- Ensuer that : Thread2 start executation only after Thread1 has completed.

- Use appropriate thread synchronization
"""
import threading
import time

def Thread1():
    print("T1 start")
    for i in range(1,51):
        print(i,end=" ")

    print()


def Thread2():
    print("T2 start")

    for i in range(50,0,-1):
        print(i,end=" ")
    print()
    
    

def main():


    start_time = time.perf_counter()

    t1 = threading.Thread(target=Thread1)

    t2 = threading.Thread(target=Thread2)

    t1.start()
    print("-"*50)

    t2.start()
    t1.join()    
    t2.join()   

    print("Exit from main...")    

    end_time = time.perf_counter()
    print(f"Time required is :{end_time - start_time:.4f} seconds ")

if __name__ == "__main__":
    main()