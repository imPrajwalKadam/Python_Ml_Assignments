"""
Write a lambda function which accept one number and return square of that number
"""

#lambda
chkSquare = lambda no: (no*no)

def main():
          no = int(input("Enter a number :"))
          ret = chkSquare(no)
          print("Square of number :",ret)
if __name__=="__main__":
          main()