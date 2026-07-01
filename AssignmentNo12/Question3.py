"""
write a program which accept two  numbers and prints addition,substraction,division and multiplications= of that number
 
"""

#lambda anonimus function ,unnamed function

Addition = lambda no,no1 : no+no1

Substraction = lambda no,no1:no - no1

Division = lambda no,no1:no%no1

multiplication = lambda no,no1:no*no1

def main():
          no = int(input("Enter a first number: "))
          no1 = int(input("Enter a second number: "))

          print("Addition is :",Addition(no,no1))
          print("Substraction is :",Substraction(no,no1))
          print("Division is :",Division(no,no1))
          print("Multiplication is :",multiplication(no,no1))
          
if __name__ == "__main__":
          main()