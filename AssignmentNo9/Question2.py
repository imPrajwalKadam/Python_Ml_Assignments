"""
Write a function which contains one functions chkGreater()  that accept two number and prints the greater number 
input : 10 20 
output :  20
"""

def chkGreater(no1,no2):
          if no1 > no2:
                    max = no1
          else:
                    max = no2
          return max           


def main():
          no1 = int(input("Enter first number :"))
          no2 = int(input("Enter second number :"))
          ret = chkGreater(no1,no2)
          print(ret,"is maximum")
          
if __name__ == "__main__":
          main()         
                    