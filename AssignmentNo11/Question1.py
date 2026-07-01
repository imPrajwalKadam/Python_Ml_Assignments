"""
Write  a program which accept one number from user and check whether that number is prime or not
Input :11
Output : Prime number
The complete list of prime numbers from 1 to 100 is:2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
"""


def chkPrime(no):
          if no < 0 :
                    no = -no
          i = 2
          tempNo = no//2
          while i <= tempNo:
                    if (no % i) == 0:
                              break
                    i=i+1
          if i == (no//2)+1:
                    return True
          else:
                    return False
                    
          

def main():
          no = int(input("Enter a number :"))
          bRet = chkPrime(no)
          if bRet == True:
                    print("Prime number ")
          else:
                    print("Not Prime number")
if __name__ == "__main__":
          main()
