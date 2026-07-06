"""
write a program which accept number from user and return its factorial
Input : 5
Outpur : 120
"""


def numFactorial(no):
    fact = 1
    for i in range(1,no+1):
        fact = fact * i
    return fact
        

def main():
    no = int(input("Enter a first number :"))
    ret = numFactorial(no)
    print(f"Factorial of number is :{ret}")
    
if __name__ == "__main__":
    main()
