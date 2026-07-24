"""
1^5 + 2^5 + 3^5+...N

for multiple values  of N simultaniously using Pool
Input :
1000000
2000000
3000000
4000000
"""
import multiprocessing,time,os

def raiseFive(no):
    val = 1
    iAdd = 0
    for i in range(1,no+1):
        iAdd += i ** 5
    return iAdd

def main():

    elemet = int(input("Enter a number :"))
    print("Enter a list elements : ")
    myList  = list()
    start_time = time.perf_counter()
    for i in range(elemet):
        myList.append(int(input()))

    pobj = multiprocessing.Pool()
    result = pobj.map(raiseFive,myList)
    pobj.close()
    pobj.join()
    end_time = time.perf_counter()
    print("result is :")
    print(result)
    print(f"Time required is : {end_time - start_time:.4f}  seconds")

if __name__ == "__main__":
    main()