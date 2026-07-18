"""
    Compair two Files (command line)

    Problem statement : Write  a program which accepts two file name through command line arguments and compair the 
    content of both files 
    - if both files contents are same display success
    - otherwise display failure
"""
import os
import sys




def compairFile(firstFile,secondFile):
    found = False
    if os.path.exists(firstFile) and os.path.exists(firstFile) :        
        try:
            fobj = open(firstFile,"r")
            sobj = open(secondFile,"r")

            fData = fobj.read()
            sData = sobj.read()

            if fData == sData:
                print("Success")
            else:
                print("Failure")
        

        except Exception as eObj:
            print(eObj)
        finally:
            fobj.close()
    else:
        print(f"{firstFile} or {secondFile} File Not exist")

def main():
  
    
    if len(sys.argv)!= 3:
        print("Invalid number of arguments")
        print("Please enter a tow file name ")

    firstFileName = sys.argv[1]
    secondFileName = sys.argv[2]

    compairFile(firstFileName,secondFileName)
if __name__ == "__main__":
    main()
