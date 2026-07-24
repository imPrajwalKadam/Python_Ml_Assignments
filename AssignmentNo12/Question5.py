"""
write a program which accept one number and  prints that many numbers in reverse order.
Input : 5
Output : 5 4 3 2 1  
"""
def DisplayRev(no):
          for i in range(no,0,-1): # Range()  funtion parameters range(start,end,step)
                print(i)    

def main():
         no = int(input("Enter a number: "))
         DisplayRev(no)

if __name__ == "__main__":
          main()