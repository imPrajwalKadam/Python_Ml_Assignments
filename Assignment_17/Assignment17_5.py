"""
Write a program which accept one number from user and check whether that number is prime or not
Date : 06/07/2026
Author:Prajwal Pradeep Kadam 
Input : 5
Output : Its Prime Number

"""

def chkPrime(no):
    if no < 0 :
        no = -no

    icnt = 2
    temp= no
    while icnt <= temp//2:
        if (temp % icnt) == 0:
            break
        icnt +=1

    if icnt == (no//2)+1:
        return True
    else:
        return False



def main():
    try:
        ino = int(input("Enter a number :"))
        ret = chkPrime(ino)


        if ret == True:
            print("Its prime number")
        else:
            print("Not prime number")
    except:
        print("number not entered")

if __name__ == "__main__":
    main()