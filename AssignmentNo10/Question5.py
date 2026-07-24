"""
Write a program which accept one number and display odd numbers till that number

Input : 10
Output : 1 3 5 7 9
"""


def DisplayOdd(no):
          if no < 0 :
                    no = -no
          for i in range(1,no+1):
                    if i % 2 != 0:
                              print(i,"\t")

def main():
          no = int(input("Enter a number :"))
          DisplayOdd(no)
          
if __name__ == "__main__":
          main()