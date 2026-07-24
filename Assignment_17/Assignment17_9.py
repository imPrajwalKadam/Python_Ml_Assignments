"""
Write a program which accept one from  user and return Count of number of digit from that number
Input : 32974821
Output : 8
"""


def CountDigit(no):
    iCnt = 0
    iDigit = 0
    while no != 0:
        iDigit = no % 10
        iCnt +=1
        no = no //10
        

       
    return iCnt
        

def main():
    no = int(input("Enter a first number :"))
    ret = CountDigit(no)
    print(f"Count of digits is :{ret}")
    
if __name__ == "__main__":
    main()
