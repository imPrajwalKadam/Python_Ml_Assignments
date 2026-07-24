"""
Write a lambda function which accept three numbers from user and return largest number
Input : 21 11 51
Outpur : 51
"""

MaxThreeNumX = lambda no1,no2,no3 : no1 if (no1 >= no2 and no1 >= no3) else (no2 if no2 >= no3 else no3)                                        

def main():
          no1 = int(input("Enter a first number :"))
          no2 = int(input("Enter a second number :"))
          no3 = int(input("Enter a third number :"))

          ret = MaxThreeNumX(no1,no2,no3)
          print("Multiplication of  number :",ret)
if __name__=="__main__":
          main()