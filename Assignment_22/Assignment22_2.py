"""
Write a program that Calculates a foctorials of multiple numbers simultaneously  using Pool.map().

Input : [10,15,20,25]
Display : - Process Id
          - Input Number
          - Factorial
"""
import multiprocessing
import time
import os


def factorNum(value):
    print(f"PID of factorNum : {os.getpid()} ")

    print("Input Number :", value)

    factoraial = 1
    for i in range(1,value+1):
        factoraial = factoraial * i
    return factoraial

def main():
    print(f"PID of Main : {os.getpid()} PPID of Main : {os.getppid()}")

    elemet = int(input("Enter a number :"))
    print("Enter a list elements : ")
    myList  = list()
    start_time = time.perf_counter()
    for i in range(elemet):
        myList.append(int(input()))

    pobj = multiprocessing.Pool()
    result = pobj.map(factorNum,myList)
    pobj.close()
    pobj.join()
    end_time = time.perf_counter()
    print("result is :")
    print(result)
    print(f"Time required is : {end_time - start_time:.4f}  seconds")

if __name__ == "__main__":
    main()