"""
write a program which accept one number and print square of that number 
input : 5
output : 25
"""

def squareX(no):
          if no < 0 :
                    no = -no
          no = no * no
          print(no)

def main():
          no = int(input("Enter a number :"))
          squareX(no)
if __name__ == "__main__":
          main()