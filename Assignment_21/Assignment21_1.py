"""
Design a python application that creates two threads named prime and non prime

- Both thread should accept list of integers .
- Prime thread should display  all prime numbers from the list
- the non prime thread should display all non-prime numbers from the list 
"""
import threading
import time



def filterPrimeData(no):    
    iCnt = 2
    while iCnt <= no // 2:
        if no % iCnt == 0:
            break
        iCnt += 1
    if iCnt == (no//2)+1:
        return True
    else:
        return False 
    
def primeThread(nums):
    for no in nums:
        if filterPrimeData(no):
            print("prime : ",no,end=" ")

def nonPrimeThread(nums):
    for no in nums:
        if filterPrimeData(no)  == False:
            print("non prime : ",no,end=" ")

def main():
    start_time = time.perf_counter()

    t1 = threading.Thread(target=primeThread,args=([1,2,3,4,5,6,7,8,9],))

    t2 = threading.Thread(target=nonPrimeThread,args=([1,2,3,4,5,6,7,8,9],))
    
    t1.start()
    t2.start()


    t1.join()
    print("-"*50)

    t2.join()   
    end_time = time.perf_counter()
    print(f"Time required is :{end_time - start_time:.4f} seconds ")

if __name__ == "__main__":
    main()