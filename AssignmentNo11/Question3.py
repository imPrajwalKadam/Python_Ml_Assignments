"""
Write a program which accept one number and prints sum of digits 
input : 123
output : 6
"""

def sumDigits(no):
          if no < 0 :
                    no = -no
          sum = 0
          digits = 0
          while no > 0:
                    
                    digits = no % 10
                    sum = sum + digits
                    no = no // 10
          return sum
                    
          


def main():
          no = int(input("Enter a number :"))
          ret = sumDigits(no)
          print("Count is:",ret)
          
if __name__ == "__main__":
          main()


