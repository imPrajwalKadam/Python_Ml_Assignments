import os
import sys

def fileExists(fileName):
    if os.path.exists(fileName):
        return True
    else:
        return False
    

def main():
    """
    Check file exists in current directory
    Problem statement : Write  a program which accepts file name from the 
    user and check whether the file is exist in the current directory or not.
    """
    if len(sys.argv) != 2:
        print("Please enter file name to check exist or not")

    else:
        fileName = sys.argv[1]
        if fileExists(fileName):
           print("File is present in current directory")
        else:
           print("There is no such file")
if __name__ == "__main__":
    main()