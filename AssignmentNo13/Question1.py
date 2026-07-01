"""
Write a program which accept length and width of rectangle and print area .
"""

#area = len * width
def DisplayAreaRectX(len,wid):
          area = len * wid    
          return area
def main():
          len = int(input("Enter a length: "))
          wid = int(input("Enter a width: "))

          ret = DisplayAreaRectX(len,wid)
          print("Area of rectangle is :",ret)
if __name__ == "__main__":
          main()