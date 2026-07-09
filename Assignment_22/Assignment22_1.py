"""
Write a program that accept a list of integers and use pool.map() to calculate sum of squares from 1 to N for for every element in the list .

Example input : [1000000,2000000,3000000,4000000]
Expacted Output : [3333338333350000,266666686666670000, 8999995500000500000, 21333325333334000000]
"""
import multiprocessing
import time

def SumSquare(value):
    squareSum = 0
    square = 1
    for i in range(value):
        square = i ** 2
        squareSum += square

    return squareSum

def main():
    elemet = int(input("Enter a number :"))
    print("Enter a list elements : ")
    myList  = list()
    start_time = time.perf_counter()
    for i in range(elemet):
        myList.append(int(input()))

    pobj = multiprocessing.Pool()
    result = pobj.map(SumSquare,myList)
    pobj.close()
    pobj.join()
    end_time = time.perf_counter()
    print("result is :")
    print(result)
    print(f"Time required is : {end_time - start_time:.4f}  seconds")

if __name__ == "__main__":
    main()