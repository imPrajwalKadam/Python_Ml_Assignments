"""
Write a program which accept N numbers from user and store it into list. return addition of all elements from that list
Input : Number of elements : 6
Input elements : 13 5 45 7 4 56
Output : 130 
"""


def ElementAddition(arr):
    add = 0
    for no in arr:
        add = add + no

    return add

def main():
    no = int(input("Enter number of elements :"))
    myList = list()
    print("Enter elements :")
    for i in range(no):
        myList.append(int(input()))
    addition = ElementAddition(myList)
    print(f"addition of list is {addition}")
if __name__ == "__main__":
    main()