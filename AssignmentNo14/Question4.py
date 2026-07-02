"""
write a lambda function which accept accept two numbers and return minimum number
"""



chkMin =lambda no1,no2 : no1 if no1 < no2 else no2 

def main():
          no1 = int(input("Enter a first number :"))
          no2 = int(input("Enter a second number :"))
          ret = chkMin(no1,no2)
          print("maximum  number :",ret)
if __name__=="__main__":
          main()