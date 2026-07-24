"""
Write a lambda function using reduce() which accept list of numbers and return a list of numbers and returns the product 
of all elements
"""
from functools import reduce

productNum = lambda no1 ,no2 : no1 * no2

def main():
    size = int(input("Enter a size of list :"))
    arr = list()
    for i in range(size):
        no = int(input())
        arr.append(no)
    prodNum = reduce(productNum,arr)
    print(prodNum)

if __name__ == "__main__":
    main() 