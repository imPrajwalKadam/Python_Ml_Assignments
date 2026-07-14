"""
Write a program that Calculates a foctorials of multiple numbers simultaneously  using Pool.map().

Input : [10,15,20,25]
Display : - Process Id
          - Input Number
          - Factorial
"""
import multiprocessing
import os


def factorNum(value):
    print(f"PID of factorNum : {os.getpid()} ")

    print("Input Number :", value)

    factoraial = 1
    for i in range(1,value+1):
        factoraial = factoraial * i
    print(f"Factorial : {factoraial}")

def main():

    pobj = multiprocessing.Pool()
    myList = [10,15,20,25]

    result = pobj.map(factorNum,myList)
    pobj.close()
    pobj.join()

if __name__ == "__main__":
    main()