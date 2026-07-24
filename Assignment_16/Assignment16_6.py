"""
Write a program which accept number from user and check whether that number is positive or negative 
Input : 11 Outut : Positive number
Input : -8 Output : Negative Number 
Input : 0 Output : Zero
"""

def ChkNum(no):
    if no == 0:
        print("Zero")
    if no > 0 :
        print("Positive Number")
    elif no < 0:
        print("Negative Number")
def main():
    no = int(input("Enter a first  number : "))


    ChkNum(no)
    
if __name__ == "__main__":
    main()