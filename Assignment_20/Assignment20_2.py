"""
Design a python application that creates two threads named evenFactor and oddFactor

- Both Thread should accept one integer number as parameter . 
- The even factor thread shuld:
    Identify even factors of the given numbers .
    Calculate and Display the sum of even factors.
- The odd factor thread should :
    Identify all odd factors of the given numbers .
    Calculate and dispay the sum of odd factors()
- After main thread complete executation , the main thread should display the message : 
    "Exit from main "

"""
import threading
import time

def evenFactorThread(no):
    print("pid of sumEven Factor thread is :",threading.get_ident())

    sum = 0
    for i in range(2,no,2):
        if no % i == 0:
            sum = sum + i
    print("Sum of even Factors : ",sum)

def oddFactorThread(no):
    print("pid of sumOdd Factor thread is :",threading.get_ident())

    sum = 0
    for i in range(1,no,2):
        if no % i == 0:
            sum = sum+i
    print("Sum of odd Factors : ",sum)

def main():

    print("pid of main thread is :",threading.get_ident())

    start_time = time.perf_counter()

    t1 = threading.Thread(target=evenFactorThread,args=(12,))

    t2 = threading.Thread(target=oddFactorThread,args=(12,))

    t1.start()
    t2.start()

    t1.join()    
    t2.join()   
    print("Exit from main...")    

    end_time = time.perf_counter()
    print(f"Time required is :{end_time - start_time:.4f} seconds ")

if __name__ == "__main__":
    main()