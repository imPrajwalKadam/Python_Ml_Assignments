"""
Write a program which contains filter () map() and reduce() in it . Python application which contains one list of numbers . List contains the numbers which are accepted from user. Filter  should filter out all such a numbers which are even.map function will calculate its square . reduce will return addition of all that number

Input List : [5,2,3,4,3,4,1,2,8,10]
List after filter : [2,4,4,2,8,10]
List after map : [4,16,16,4,64,100]
output of reduce : 204
"""
from functools import reduce 

powerNoReduce = lambda no1 ,no2: no1 + no2 

filterData = lambda no1:True if no1 %2 == 0 else False 

mapData = lambda no1 : no1 * no1

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