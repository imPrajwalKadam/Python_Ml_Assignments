"""
Write a program which accept one number from user and display below pattern
Input : 5
Output :    
            1 
            1 2 
            1 2 3
            1 2 3 4 
            1 2 3 4 5 
"""


def Display(no):
    for i in range(1,no+1):
        for j in range(1,no+1):
            if j <= i:
                print(j,end=" ")
        print()
def main():
    no = int(input("Enter a number "))
    Display(no)

if __name__ == "__main__":
    main()