"""
Q4- Copy File contents into Another File


Input : ABC.txt
Expected Output : Demo.txt
"""
import os



def DisplayFileContaint(srcFile,DestFile):
    if os.path.exists(srcFile):        
        try:
            fobj = open(srcFile,"r")
            wObj = open(DestFile,"w")


            line = fobj.readline()
            while len(line) >0:
                wObj.write(line)
                line = fobj.readline()
            print(f"containt of {srcFile} is copied into {DestFile} file")
        except Exception as eObj:
            print(eObj)
        finally:
            fobj.close()
            wObj.close()
    else:
        print(f"{srcFile} File Not exist")

def main():
    """
    Write program which accepts two  file names from the user
    -First file is existing file 
    -second fiile is new
    Copy all contents from first file into the second file 
    """
    

    firstName = str(input("Enter the first file name (existing file): "))
    secondFile = str(input("Enter the second file name (new file) :"))
    DisplayFileContaint(firstName,secondFile)
    
if __name__ == "__main__":
    main()
