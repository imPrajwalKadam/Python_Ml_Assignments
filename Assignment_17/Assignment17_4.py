"""
Write a program which accept one from  user and return addition of its factors
Input : 12
Output : 16 (1+2+3+4+6)
"""


def AdditionFactors(no):
    Addition = 0
    for i in range(1,no):
        if no%i == 0:
             Addition = Addition + i
    return Addition
        

def main():
    no = int(input("Enter a first number :"))
    ret = AdditionFactors(no)
    print(f"Addition of factors is :{ret}")
    
if __name__ == "__main__":
    main()
