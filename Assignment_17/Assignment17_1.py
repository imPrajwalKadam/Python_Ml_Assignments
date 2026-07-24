"""
Create a module named as Arithmatic which contains  4 functions as add() for addition, sub() for substraction , mult() for multiplication, and div() for division . All functions accept two parameters as number and perform the operations . Write one python program which call all the functions from arithmatic module by accepting the parameters from user
"""
from Arithmatic_module import add,sub,mult,div


def Display(no1,no2):
    Addition = add(no1,no2)
    Substraction = sub(no1,no2)
    multiplication = mult(no1,no2)
    division = div(no1,no2)

    print(f"Addition of {no1} and {no2} is {Addition}")
    print(f"Substraction of {no1} and {no2} is {Substraction}") 
    print(f"Multiplication of {no1} and {no2} is {multiplication}")
    print(f"Division of {no1} and {no2} is {division}")


def main():
    no1 = int(input("Enter a first number :"))
    no2 = int(input("Enter a second number : "))
    Display(no1,no2)

    
if __name__ == "__main__":
    main()
