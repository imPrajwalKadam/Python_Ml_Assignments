"""
Write a program which accept number and print sum of first N natural number 
input : 5
output :15
"""


def NaturalAddition(no):
          if no < 0 :
                    no = -no
          nAddition = 0
          for i in range(1,no+1):
                    nAddition = i + nAddition
                    
          return nAddition
def main():
          no = int(input("Enter a number :"))
          ret = NaturalAddition(no)
          print("Addition of natural number is :",ret)
if __name__ == "__main__":
          main()