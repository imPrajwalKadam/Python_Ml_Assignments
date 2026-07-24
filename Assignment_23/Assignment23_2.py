"""

Write a python program using multiprocessing.Pool to calculate the sum of all odd numbers from 1 to N for every number from the every given list

Expected Task :For each number N , Calculates
        1+3+5+7+9 + .... + N
        
Expected Output Formate : 
        Process Id:1234
        Input Number : 1000000
        Sum of Even Numbers : 2500000000        
"""


import multiprocessing
import os


def OddNum(no):
    print(f"Processs Id :{os.getpid()} ")
    print(f"Input number : {no}")
    add = 0
    for i in range(1,no+1):
        if i %2 != 0:
            add = add + i
    print(f"Sum of even number : {add}")

def main():
    pobj = multiprocessing.Pool()
    myList = [100000,200000,300000,400000]
    pobj.map(OddNum,myList)
    pobj.close()

    pobj.join()

if __name__ == "__main__":
    main()