"""
Write a program which contains lambda function which accept two parameter and return its multiplication

Input : 4   3   Output : 12
Input : 6   3   Output : 18 
"""


powerNo = lambda no1 ,no2: no1 * no2 
def main():
    no1 = int(input("Enter a first number : "))
    no2 = int(input("Enter a second number : "))

    ret = powerNo(no1,no2)
    print(f"multiplication is : {ret}")

if __name__ == "__main__":
    main()