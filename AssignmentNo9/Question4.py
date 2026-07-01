"""
write a program which accept one number and print cube of that number 
"""

def chkCube(no):
          cube = 1
          for i in range(1,4):
                    cube = no * cube
          print(cube)

def main():
          no = int(input("Enter a number : "))
          chkCube(no)
if __name__ == "__main__":
          main()