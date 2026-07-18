"""
copy File content into new file (command line)

    Problem statement : Write  a program which accepts existing file name from the 
    command line arguments create new file named ABC.txt,and copy all content from 
    the given file into ABC.txt 
"""
import os
import sys


def copyFileContaint(srcFile):
    DestFile = "ABC.txt"
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
    if len(sys.argv) != 2:
        print("Please enter a text file name ")
    else:
        fName = sys.argv[1]
        copyFileContaint(fName)
    
if __name__ == "__main__":
    main()
