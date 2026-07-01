"""
Write a program which accept one number and check whether it is perfect or not  
Input : 6
Output : Perfect Number
"""

def chkPerfect(no):
          if no < 0:
                    no = -no
          i = 0
          temp = no
          add = 0
          while no !=i:
                    i +=1
                    if no % i ==0:
                              add = i+add
          chk =  add - no   
          if chk == temp:
                    return True
          else:
                    return False
                           
def main():
          no = int(input("Enter a length: "))

          bRet = chkPerfect(no)
          if bRet == True:
                    print("Perfect number")
          else:
                    print("Not Perfect number")
if __name__ == "__main__":
          main()