"""
Write a lambda function using reduce() which accept list of numbers and return a list of numbers and return a Addition of All elements
"""
from functools import reduce

AddNum = lambda no1,no2: no1 + no2

def main():
    size = int(input("Enter a size of list :"))
    arr = list()
    for i in range(size):
        no = int(input())
        arr.append(no)
    sum = reduce(AddNum,arr)
    print(sum)

if __name__ == "__main__":
    main() 