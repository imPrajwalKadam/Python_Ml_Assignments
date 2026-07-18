"""
Q3- Display the file line by line 

Input : Demo.txt

Expected Output : 
Total number of words in Demo.txt
"""
import os



def DisplayFileContaint(FileName):
    if os.path.exists(FileName):
        
        try:
            fobj = open(FileName,"r")
            line = fobj.readline()
            while len(line) >0:
                print(line,end = "")
                line = fobj.readline()

        except Exception as eObj:
            print(eObj)
        finally:
            fobj.close()

    else:
        print("File Not exist")

def main():
    """
    Write program which accepts a file name from the user and displays content of the file line by line 
    on the screem.
    """
    

    fName = str(input("Enter file Name :"))
    DisplayFileContaint(fName)
    
if __name__ == "__main__":
    main()
