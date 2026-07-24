"""
Write a program which accept N numbers from user and store it into list. return maximum number from that list
Input : Number of elements : 6
Input elements : 13 5 45 7 4 56
Output : 56 
"""


def ElementMax(arr):
    max = 0
    for no in arr:
        if no > max:
            max = no

    return max

def main():
    no = int(input("Enter number of elements :"))
    myList = list()
    print("Enter elements :")
    for i in range(no):
        myList.append(int(input()))
    max = ElementMax(myList)
    print(f"maximum of list is {max}")
if __name__ == "__main__":
    main()