"""
Write a program which contains lambda function which accept one parameter and return power of two 

Input : 4 Output : 16
Input : 6 Output : 64 
"""


powerNo = lambda no: 2 ** no 
def main():
    no = int(input("Enter a number : "))
    ret = powerNo(no)
    print(f"power of no is : {ret}")

if __name__ == "__main__":
    main()