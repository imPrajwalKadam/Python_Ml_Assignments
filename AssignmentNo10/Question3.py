"""
write a program which accept one number and print factorials of that number 
input : 5
output : 120   

5 * 4 = 20
20 * 3 = 60
60 * 2 = 120
120 * 1 = 120

"""

def DisplayFact(no):
          if no < 0 :
                    no = -no
          fact = no
          for i in range(no-1,0,-1):
                    fact = fact * i
          return fact

def main():
          no = int(input("Enter a number :"))
          factNum = DisplayFact(no)
          print("Factorial number is:",factNum)
          
if __name__ == "__main__":
          main()