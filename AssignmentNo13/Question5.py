"""
Write a program which accept marks and display grade 
Condition example:
>= 75 ->Distinction
>= 65 ->First Class
>=50 -> Second Class
<50 -> Fail
"""

def DisplayGrade(marks):
          if marks >= 75:
                    print("Distinction")
          elif marks>=65:
                    print("First Class")
          elif marks >= 50:
                    print("Second Class")
          else:
                    print("Fail")
                    
          

def main():
          marks = int(input("Enter a Marks: "))

          DisplayGrade(marks)
if __name__ == "__main__":
          main()