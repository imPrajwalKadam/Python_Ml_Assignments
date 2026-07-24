"""
Write a program which accept one number from user and display below pattern     

Output :    * * * * *
            * * * * *
            * * * * *
            * * * * *
            * * * * *
"""



def Display(no):
    for _ in range(1,no+1):
        for _ in range(1,no +1):
            print("*",end=" ")    
        print()
        

def main():
    no = int(input("Enter a first number :"))
    Display(no)

    
if __name__ == "__main__":
    main()
