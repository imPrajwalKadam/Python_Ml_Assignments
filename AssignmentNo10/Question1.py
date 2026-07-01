"""
Write a program which accept one number and print multiplication table of that number

input : 4
output : 4 8 12 16 20 24 28 32 36 40
"""


def MultTableX(no):
          if no < 0 :
                    no = -no
          multVal = 1
          for i in range(1,11):
                    multVal = no * i
                    print(multVal)
def main():
          no = int(input("Enter a number :"))
          MultTableX(no)

if __name__ == "__main__":
          main()