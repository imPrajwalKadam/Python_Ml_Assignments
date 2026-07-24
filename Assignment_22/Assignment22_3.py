"""
for every number in given list ,count how many prime numbers  exist between  1 and N using multiprocessing  Pool
Example :
10000
20000
30000
40000
Display total prime count for each number. 
"""

import multiprocessing
import time
import os


def chkPrime(value):
    
    i = 2

    while i <= value//2:
        if value % i == 0:
            break
        i +=1

    if i == (value // 2) +1:
        return True
    else:
        return False

def countPrime(no):
    cnt = 0
    for i in range(1,no):
        if chkPrime(i):
            cnt +=1
    return cnt      

def main():
    print(f"PID of Main : {os.getpid()} PPID of Main : {os.getppid()}")

    elemet = int(input("Enter a number :"))
    print("Enter a list elements : ")
    myList  = list()
    start_time = time.perf_counter()
    for i in range(elemet):
        myList.append(int(input()))

    pobj = multiprocessing.Pool()
    result = pobj.map(countPrime,myList)
    pobj.close()
    pobj.join()
    end_time = time.perf_counter()
    print("result is :")
    print(result)
    print(f"Time required is : {end_time - start_time:.4f}  seconds")

if __name__ == "__main__":
    main()