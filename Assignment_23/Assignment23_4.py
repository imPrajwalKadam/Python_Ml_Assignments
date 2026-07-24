"""

Write a python program that count how many odd numbers  exist between 1 and N  using Pool.map()
Input :  [1000000,2000000,3000000,4000000]        
Expected Output Formate : 
        Process Id:1237
        Input Number : 1000000
        count of Odd Numbers : 500000000        
"""


import multiprocessing
import os


def CountOdd(no):
    print(f"Processs Id :{os.getpid()} ")
    print(f"Input number : {no}")
    oddCounter = 0
    for i in range(1,no+1):
        if i %2 == 0:
            oddCounter += 1
    print(f"count of Odd numbers : {oddCounter}")

def main():
    pobj = multiprocessing.Pool()
    myList = [1000000,2000000,3000000,4000000]
    pobj.map(CountOdd,myList)

    pobj.close()

    pobj.join()

if __name__ == "__main__":
    main()