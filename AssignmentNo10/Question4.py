"""
Write a program accept a number from user and display the even numbers till that number
input : 10
output : 2 4 6 8 10
"""


def DisplayEven(no):
          if no < 0 :
                    no = -no
          for i in range(1,no+1):
                    if i % 2 == 0:
                              print(i,"\t")
                    

def main():
          no = int(input("Enter a number :"))
          DisplayEven(no)
          
if __name__ == "__main__":
          main()