"""
Write a program which accept one nnumber and prints that many number starting from 1

Input : 5
Output : 1 2 3 4 5 
"""

def Display(no):
          for i in range(1,no+1):
                    print(i)


def main():
         no = int(input("Enter a number: "))
         Display(no)

if __name__ == "__main__":
          main()