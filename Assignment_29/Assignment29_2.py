import os
import sys

def DisplayFileContent(fileName):
    if os.path.exists(fileName):
        fobj = open(fileName,"r")
        data = fobj.read()
        print(data)
    else:
        print("File not exist !!!")    

def main():
    """
    Display File content
    Problem statement : Write  a program which accepts file name from the 
    user,Open the file, and display the entire contents on the console.
    """
    if len(sys.argv) != 2:
        print("Please enter file name to check exist or not")

    else:
        fileName = sys.argv[1]
        DisplayFileContent(fileName)
        
if __name__ == "__main__":
    main()