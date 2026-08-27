"""
Write a python program that calculate the vareiance and standard deviation of 
the dataset  
[6,7,8,9,10,11,12]

Display boath result
"""

import pandas as pd

def main():
    data  = [6,7,8,9,11,12]
    df = pd.Series(data)
    print("varieiance of dataframe : ",df.var())
    print("Standerd deviation : ", df.std())
if __name__ == "__main__":
    main()
