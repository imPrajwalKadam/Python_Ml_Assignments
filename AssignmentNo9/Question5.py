"""
Write a program which accept one number from user and check that number divisible by 3 and 5
"""

def chkDivisible(no):
          #filter
          if no < 0 :
                    no = -no
                    
          if (no % 3 == 0) and (no % 5 == 0):
                    return True
          else:   
                    return False 
def main():
          no = int(input("Enter a number : "))
          bRet = chkDivisible(no)
          if bRet == True:
                    print("Divisible by 3 and 5")
                    
if __name__ == "__main__":
          main()