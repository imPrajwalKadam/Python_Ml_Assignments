"""
Write a program accept one number and print its factors
Input : 12
Output: 1 2 3 4 6 12
"""



def DisplayFactor(no):
          i = 0
          while i != no:
                    i+=1 
                    if no % i ==0:
                              print(i)


def main():
         no = int(input("Enter a number: "))
         DisplayFactor(no)

if __name__ == "__main__":
          main()