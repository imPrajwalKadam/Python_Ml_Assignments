"""
Write a program which accept one number from user and print that number of "*"  on screen 

Input: 5 Output : * * * * * 
"""

def Display(no):
    for _ in range(no):
        print('*',end=" ")


def main():
    no = int(input("Enter number :"))
    Display(no)
    
if __name__ == "__main__":
    main()