"""
Write a lambda function using reduce() which accept list of numbers and return a list of numbers and returns maximum elements
"""
from functools import reduce

# AddNum = lambda no1,no2: max(no1,no2)
AddNum = lambda no1 ,no2 : no1 if no1 > no2 else no2
def main():
    size = int(input("Enter a size of list :"))
    arr = list()
    for i in range(size):
        no = int(input())
        arr.append(no)
    maxNum = reduce(AddNum,arr)
    print(maxNum)

if __name__ == "__main__":
    main() 