"""
Write a program which contains one function named as chkNum() which accept two numbers from user and return adddition of that two numbers 
Input   : 11 5
Output  : 16
"""




def AddNum(no1,no2):
    return no1 + no2
    

def main():
    no1 = int(input("Enter a first  number : "))
    no2 = int(input("Enter a second number : "))

    ret = AddNum(no1,no2)
    print("Addition of number is :",ret)
    
if __name__ == "__main__":
    main()