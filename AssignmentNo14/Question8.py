"""
Write a lambda function which accept two numbers and return addition.
"""



AddNum =lambda no1,no2 : no1+no2 

def main():
          no1 = int(input("Enter a first number :"))
          no2 = int(input("Enter a second number :"))
          ret = AddNum(no1,no2)
          print("Addition of  number :",ret)
if __name__=="__main__":
          main()