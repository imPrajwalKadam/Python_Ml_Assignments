"""
Write a lambda function which is accept one number and return true if divisible by 5.  
"""






chkDivisible = lambda no: True if no % 5 == 0 else False

def main():
          no1 = int(input("Enter a first number :"))
          ret = chkDivisible(no1)
          if ret == True:
                    print("number divisible by 5")
          else:
                    print("number NOT divible by 5")
if __name__=="__main__":
          main()