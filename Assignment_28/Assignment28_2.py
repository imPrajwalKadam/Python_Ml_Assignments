"""
Q2- Count words in file 

Input : Demo.txt

Expected Output : 
Total number of words in Demo.txt
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

    def CountWords(self):
        if not(self.ChkFileExist()):
            return f"There is no such a file {self.FileName}"
        
        try:
            fObj = open(self.FileName,"r")
            words = fObj.read().split()
            return len(words)
        except Exception as eObj:
            return eObj
        finally:
            fObj.close()         
       


def main():
    # Write program which accepts a file name from the user and counts total number of words in that file.

    fName = str(input("Enter file Name :"))
    fObj = FileOperations(fName)

    wordsCnt = fObj.CountWords()
    try:
        if int(wordsCnt):
            print(f"Total number of Words in {fName} {wordsCnt}")
    except ValueError as vObj:
        print(wordsCnt)

if __name__ == "__main__":
    main()
