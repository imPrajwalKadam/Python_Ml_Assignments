"""
Write a lambda function using map() which accept list of number and return list of squares of each number
"""

#lambda
chkSquare = lambda no: (no*no)

def main():
    size = int(input("Enter length of list :"))
    myList = list()
    print("Enter a array elements : ")
    for i in range(size):
        no = int(input())
        myList.append(no)
    mapList =list(map(chkSquare,myList))
    print(mapList)

if __name__ == "__main__":
    main()