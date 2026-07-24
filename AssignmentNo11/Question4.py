"""
Write a program which accept one number from user and reverse that number 
input : 123
output : 321
"""

def revDigits(no):
          if no < 0 :
                    no = -no
          sum = 0
          digits = 0
          rev = 0
          while no > 0:
                    digits = no % 10
                    sum = sum + digits
                    # rev += str(digits)
                    rev = (rev*10)+digits
                    no = no // 10
          return rev
                    
          


def main():
          no = int(input("Enter a number :"))
          ret = revDigits(no)
          print(ret)
          
if __name__ == "__main__":
          main()


