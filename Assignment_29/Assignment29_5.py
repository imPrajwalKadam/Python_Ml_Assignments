"""
    Frequency of a string in file 

    Problem statement : Write  a program which accepts  file name and one string from the user and return the frequency
    (count of occurrences)  of that string in the file.
    input : Demo.txt Marvellous

    Expected output : Count how many times "Marvellous" appears in Demo.txt

"""
import os,sys

def countWord(srcFile,searchWord):
    found = False
    count = 0
    if os.path.exists(srcFile):        
        try:
            fobj = open(srcFile,"r")

            line = fobj.readline()
            while len(line) >0:
                words = line.split(" ")
                for word in words:
                    if searchWord == word.replace("\n",""):
                        found = True
                        count+=1
                                        
                line = fobj.readline()

            print(f"{searchWord} count is {count}")
        except Exception as eObj:
            print(eObj)
        finally:
            fobj.close()
    else:
        print(f"{srcFile} File Not exist")

def main():
    
    if len(sys.argv)!= 3:
        print("Invalid number of arguments")
        print("Please enter a file name and word that you want to search")

    fileName = sys.argv[1]
    wordSearch = sys.argv[2]

    countWord(fileName,wordSearch)
if __name__ == "__main__":
    main()
