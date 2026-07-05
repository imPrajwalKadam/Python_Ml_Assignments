"""
Write a program which contains one function That accept one number from user and return true if number is divisible by 5 otherwise return false
Input : 8 Outpue: False
Input : 5 Output : True
"""


def ChkDiv5(no):
   if no % 5 == 0:
       return True
   else:
       False
       
def main():
    no = int(input("Enter a first  number : "))


    bret = ChkDiv5(no)
    if bret == True:
        print("True")
    else:
        print("False")
    
if __name__ == "__main__":
    main()
