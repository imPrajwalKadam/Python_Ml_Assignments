"""

Write a python program that count how many odd numbers  exist between 1 and N  using Pool.map()
Input :  [1000000,2000000,3000000,4000000]        
Expected Output Formate : 
        Process Id:1234
        Input Number : 1000000
        count of Even Numbers : 5000000        
"""


import multiprocessing
import os


def CountEven(no):
    print(f"Processs Id :{os.getpid()} ")
    print(f"Input number : {no}")
    evenCounter = 0
    for i in range(1,no+1):
        if i %2 == 0:
            evenCounter += 1
    print(f"count of even numbers : {evenCounter}")

def main():
    pobj = multiprocessing.Pool()
    myList = [1000000,2000000,3000000,4000000]
    pobj.map(CountEven,myList)
    pobj.close()

    pobj.join()

if __name__ == "__main__":
    main()