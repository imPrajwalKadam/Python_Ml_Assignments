"""
Write a lambda function using filter() which accept list  of strings and return a list strings having length greater then 5
"""
from functools import reduce

LenFive = lambda val: True  if len(val) > 5 else False

def main():
    size = int(input("Enter a size of list :"))
    arr = list()
    for i in range(size):
        sVal = str(input())
        arr.append(sVal)

    filterList = list(filter(LenFive,arr))
    print(filterList)

if __name__ == "__main__":
    main() 