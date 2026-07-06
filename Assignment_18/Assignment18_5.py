"""
Write a program which accept N numbers from user and store it into list. Accept one another number from user and return frequency of that number from list 
Input : Number of elements : 6
Input elements : 13 5 45 5 4 56
Element To search : 5
Output : 2
"""


def ElementSearch(arr,no):
    cnt = 0
    for num in arr:
        if num == no:
            cnt+=1

    return cnt

def main():
    no = int(input("Enter number of elements :"))
    myList = list()
    print("Enter elements :")
    for i in range(no):
        myList.append(int(input()))
    num = int(input("Enter a number to search :"))
    ret = ElementSearch(myList,num)

    print(f" count of number is {ret}")
if __name__ == "__main__":
    main()