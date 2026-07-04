"""
Write a lambda function using filter() which accept list of numbers and return a list of numbers and return a list 
of numbers divisible by both  3 and 5 
"""
from functools import reduce

chkNo = lambda no: True if no % 2 == 0 else False

def main():
    size = int(input("Enter a size of list :"))
    arr = list()
    for i in range(size):
        no = int(input())
        arr.append(no)

    filterList = list(filter(chkNo,arr))
    print(filterList)

if __name__ == "__main__":
    main() 

