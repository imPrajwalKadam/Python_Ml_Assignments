"""
Q5- Search a word in File


Input : Demo.txt  Marvellous
Expected Output : Display whether the word is present in the file or not 
"""
import os
import sys


def searchWord(srcFile,searchWord):
    found = False
    if os.path.exists(srcFile):        
        try:
            fobj = open(srcFile,"r")

            line = fobj.readline()
            while len(line) >0:
                words = line.split(" ")
                for word in words:
                    if searchWord == word.replace("\n",""):
                        found = True
                        break
                if found:
                    break
                                        
                line = fobj.readline()

            if found:
                print(f"Word {searchWord} found in {os.path.basename(srcFile)}")
            else:
                print(f"Word {searchWord} not found in {os.path.basename(srcFile)}")

        except Exception as eObj:
            print(eObj)
        finally:
            fobj.close()
    else:
        print(f"{srcFile} File Not exist")

def main():
    """
    Write program which accepts  file names and word from the user and check whether that word is present 
    in the file or not
    
    """
    
    if len(sys.argv)!= 3:
        print("Invalid number of arguments")
        print("Please enter a file name and word that you want to search")

    fileName = sys.argv[1]
    wordSearch = sys.argv[2]

    searchWord(fileName,wordSearch)
if __name__ == "__main__":
    main()
