"""
Design a python application that creates two threads 

-   Thread 1 should calculate display  the maximum element from the list
-   Thread 2 should calculate display  the minimum element from the list
The list should be accepted by the user .
"""
import threading
import time



    
def sumEleThread(nums):
    sum = 0
    for no in nums:
        sum = sum + no
    print("sum of elements  is :",sum)

def prodEleThread(nums):
    prod = 1
    for no in nums:
        prod = prod ** no
    print("product of elements are: ",prod)


def main():

    lenElement = int(input("Enter a list length :"))

    myList = list()

    print("Enter a elements :")
    for i in range(lenElement):
        myList.append(int(input()))
    
    start_time = time.perf_counter()

    t1 = threading.Thread(target=sumEleThread,args=(myList,))

    t2 = threading.Thread(target=prodEleThread,args=(myList,))
    
    t1.start()
    t2.start()


    t1.join()
    print("-"*50)

    t2.join()   
    end_time = time.perf_counter()
    print(f"Time required is :{end_time - start_time:.4f} seconds ")

if __name__ == "__main__":
    main()