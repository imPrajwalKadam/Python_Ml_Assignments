"""
Write a program which accept one from  user and return Addition digit from that number
Input : 32974821
Output : 8
"""


def AdditionDigit(no):
    iAdd = 0
    iDigit = 0
    while no != 0:
        iDigit = no % 10
        iAdd = iAdd + iDigit
        no = no //10
        
    return iAdd
        

def main():
    no = int(input("Enter a first number :"))
    ret = AdditionDigit(no)
    print(f"Addition of digits is :{ret}")
    
if __name__ == "__main__":
    main()
