"""
Write a program which accept one number and print  count of the digits from that number 
input :7521
output: 4
"""


def displayCount(ino):
          if ino < 0 :
                    ino = - ino
          iCnt = 0
          
          while ino > 0:
                    iDigit = ino % 10

                    iCnt = iCnt +1                    
                    ino = ino // 10
          return iCnt

def main():
          no = int(input("Enter a number :"))
          ret = displayCount(no)
          print("Count is:",ret)
if __name__ == "__main__":
          main()