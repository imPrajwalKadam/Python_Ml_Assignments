"""
Write a program which accept N numbers from user and store it into list. Return addition of all primes from that list .Main python file accept N number from user and pass each number to chkPrime() function which is part of our user defined module named as MarvellousNum . Name of the function from main python file should be ListPrime().

Input : Number of elements : 11
Input elements : 13 5 45 7 4 56 10 34 2 5 8
Output : 54(13 + 5 + 7 + 2 + 5)
"""


def chkPrime(no):
    cnt = 2
    temp = no
    while cnt <= no//2:
          if no % cnt == 0:
              break
          cnt += 1

    if cnt == (temp // 2)+1:
        return True
    else:
        return False

def ListPrime(arr):
    addition = 0
    primeList = list()
    for no in arr:
        if chkPrime(no):
            primeList.append(no)
            addition = addition + no
    print(primeList)
    return addition

def main():
    no = int(input("Enter number of elements :"))
    myList = list()
    print("Enter elements :")
    PrimeList = []

    for i in range(no):
        no = int(input())
        myList.append(no)
    ret = ListPrime(myList)
    
    print(f" addition of prime numbers is {ret}")
if __name__ == "__main__":
    main()