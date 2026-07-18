"""
Q1- Count lines in file 
Write program which accepts a file name from the user and counts how many lines are present 
in file.

Input : Demo.txt
Expected Output : 
Total number of lines in Demo.txt
"""
import os


class FileOperations:
    def __init__(self,fileName):
        self.FileName = fileName
        
    def ChkFileExist(self):
        if os.path.exists(self.FileName):
            return True
        else:
            return False

    def CountLines(self):

        if not(self.ChkFileExist()):
            return f"There is no such a file {self.FileName}"
        
        try:
            fObj = open(self.FileName,"r")
            lines = fObj.readlines()
            return len(lines)
        except Exception as eObj:
            return eObj
        finally:
            fObj.close()         
       


def main():
    fName = str(input("Enter file Name :"))
    fObj = FileOperations(fName)

    lines = fObj.CountLines()
    try:
        if int(lines):
            print(f"Total number of lines in {fName} {lines}")
    except ValueError as vObj:
        print(lines)

if __name__ == "__main__":
    main()
