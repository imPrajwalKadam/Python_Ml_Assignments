"""
Write a program which accept one character from user and checks whether  it is vowel or not 

Input : a
Output : vowel
"""



def chkVowel(ch):
          myList = ['a','e','i','o','u']
          ch = ch.lower()
          if ch in myList:
                    return True
          else:
                    return False
          
def main():
          myCh = str(input("Enter  a character :"))
          bRet = chkVowel(myCh)
          if bRet == True:
                    print("Vowel")
          else:
                    print("Not Vowel")


if __name__ == "__main__":
          main()