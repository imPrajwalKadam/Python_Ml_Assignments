"""
Write a program which displays first 10 even number s on screen
Output : 2 4 6 8 10 12 14 16 18 20

"""


def DisplayEven10():
    for i in range(2,20+1,2):
        print(i,end=" ")

def main():
    DisplayEven10()
    
if __name__ == "__main__":
    main()