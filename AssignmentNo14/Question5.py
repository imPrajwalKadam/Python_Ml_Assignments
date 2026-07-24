"""
Write a lambda function which accept one number and returns True if number is even otherwise return false 
"""




chkEvenOdd = lambda no: True if no % 2==0 else False

def main():
          no1 = int(input("Enter a first number :"))
          ret = chkEvenOdd(no1)
          if ret == True:
                    print("Even Number")
          else:
                    print("Odd Number ")
if __name__=="__main__":
          main()