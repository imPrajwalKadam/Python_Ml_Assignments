"""

Write a python program using multiprocessing.Pool to calculate the sum of all even numbers from 1 to N for every number from the every given list

Expected Task :For each number N , Calculates
        2+4+6+8+10 + .... + N

Expected Output Formate : 
        Process Id:1234
        Input Number : 1000000
        Sum of Even Numbers : 2500050000        
"""


import multiprocessing
import os


def EvenNum(no):
    print(f"Processs Id :{os.getpid()} ")
    print(f"Input number : {no}")
    add = 0
    for i in range(1,no+1):
        if i %2 == 0:
            add = add + i
    print(f"Sum of even number : {add}")

def main():
    pobj = multiprocessing.Pool()
    myList = [100000,200000,300000,400000]
    pobj.map(EvenNum,myList)
    pobj.close()
    pobj.join()

if __name__ == "__main__":
    main()