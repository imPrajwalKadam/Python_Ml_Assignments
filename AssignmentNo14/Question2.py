"""
write a lambda function which accept one number and returns cube of that number.
"""


chkCube =  lambda no :(no*no*no)
def main():
          no = int(input("Enter a number :"))
          ret = chkCube(no)
          print("Square of number :",ret)
if __name__=="__main__":
          main()