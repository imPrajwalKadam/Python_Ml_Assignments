"""
Write a program which contains filter () map() and reduce() in it . Python application which contains one list of numbers . List contains the numbers which are accepted from user. Filter  should filter out all such a numbers which greater then equal to 70. and less then or equal to 90. Map function will   incress each number by 10 . Reduce will return product of all that numbers.

Input List : [4,34,36,76,68,24,89,23,86,90,45,70]
List after filter : [76,89,86,90,70]
List after map : [86,99,96,100,80]
output of reduce : 6538752000
"""
from functools import reduce 

powerNoReduce = lambda no1 ,no2: no1 ** no2 

filterData = lambda no1:True if no1 >= 70 and no1 <= 90 else False 

mapData = lambda no1 : no1 +10

def main():
    try:

        no = int(input("enter list length :"))
        myList = list()
        for i in range(no):
            iNO = int(input())
            myList.append(iNO)
        print(myList)
        fList = list(filter(filterData,myList))
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