"""
Write a program which contains filter () map() and reduce() in it . Python application which contains one list of numbers . List contains the numbers which are accepted from user. Filter  should filter out all such a prime numbers.map function will multiply each number by 2 . reduce will return maximum number from that numbers(You can use normal function insted of lambda function .)


Input List : [2,70,11,10,17,23,31,77]
List after filter : [2,11,17,23,31]
List after map : [4,22,34,46,62]
output of reduce : 62
"""
from functools import reduce 


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


mapData = lambda no1 : no1 * 2

powerNoReduce = lambda no1 ,no2: no1 if no1 > no2 else no2 



def main():
    try:

        no = int(input("enter list length :"))
        myList = list()
        for i in range(no):
            iNO = int(input())
            myList.append(iNO)
        print(myList)
        fList = list(filter(filterPrimeData,myList))
        print("List After Filter :")
        print(fList)

        mList = list(map(mapData,fList))
        print("List After Map :")
        print(mList)


        reduceVal = int(reduce(powerNoReduce,mList))
        print("output of reduce :")
        print(reduceVal)
    except Exception as e:
        print(f"Exception occured {e}")



if __name__ == "__main__":
    main()