"""
Write a program which accept number from user and check whether palendrom or not 
Input : 121
Output : Palindrome
"""

def chkPalindrome(no):
          if no < 0:
                    no = -no
          iDigit = 0
          rev = 0
          temp = no
          while no > 0:
                    iDigit = no % 10
                    rev = (rev*10) + iDigit
                    no = no //10
          # print("rev :",rev,"temp :",temp,"no :",no)
          
          if rev == temp:
                    return True
          else:
                    return False
                    
def main():
          no = int(input("Enter a number :"))
          bRet = chkPalindrome(no)
          if bRet == True:
                    print("Palindrome")
          else:
                    print("Not Palindrome")
          
if __name__ == "__main__":
          main()




