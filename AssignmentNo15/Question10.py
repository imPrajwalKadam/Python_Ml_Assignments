"""
Write a lambda function using filter() which accept list of numbers and return a list of numbers and return the count 
of even numbers 
"""

chkNo = lambda no: True if no % 2 == 0 else False

def main():
    size = int(input("Enter a size of list :"))
    arr = list()
    for i in range(size):
        no = int(input())
        arr.append(no)

    filterList = list(filter(chkNo,arr))
    print(len(filterList))

if __name__ == "__main__":
    main() 

