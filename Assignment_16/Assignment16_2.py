"""
Write a program which contains one function named as chkNum() which
accept one parameter as number . If number is even then it should Display
"Even Number" otherwise display "odd number" on console.
Input : 11 Output: Odd number
Input : 8  Output :Even Number
"""


def chkNum(no):
    if no% 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

def main():
    no = int(input("Enter a number "))
    chkNum(no)
if __name__ == "__main__":
    main()