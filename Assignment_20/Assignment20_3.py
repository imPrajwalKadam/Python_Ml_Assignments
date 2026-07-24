"""
Design a python application that creates two threads named evenList and oddList

- Both Thread should accept List of integers as input .

- The evenList thread shuld:
    Extract all even elements from the list .
    Calculate and Display their sum.

- The oddList thread shuld:
    Extract all odd elements from the list .
    Calculate and Display their sum.

- Thread should run concurrently

"""
import threading
import time

def evenThread(no):
    sum = 0
    print("-"*50)
    for i in range(2,no,2):
        sum = sum + i
        print(i)
    print("Sum of even  : ",sum)

def oddThread(no):
    sum = 0
    print("-"*50)

    for i in range(1,no,2):
        sum = sum+i
        print(i)
    print("Sum of odd : ",sum)

def main():


    start_time = time.perf_counter()

    t1 = threading.Thread(target=evenThread,args=(10,))

    t2 = threading.Thread(target=oddThread,args=(10,))

    t1.start()
    t2.start()

    t1.join()    
    t2.join()   
    print("Exit from main...")    

    end_time = time.perf_counter()
    print(f"Time required is :{end_time - start_time:.4f} seconds ")

if __name__ == "__main__":
    main()