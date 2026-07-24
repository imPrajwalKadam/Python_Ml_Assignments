"""
Write  a program which accept name from user and display length of its name
Input : "Marvellous"
Output : 10
"""

def DisplayLen(myStr):
    print(len(myStr))

def main():
    myStr = str(input("Enter a string : "))
    DisplayLen(myStr)
    
if __name__ == "__main__":
    main()