"""
Write a python program that calcuate the mean of dataset using 
numpy for the following values.
[6,7,8,9,10,11,12] 
"""
import pandas as pd



def main():
    
    border = 50 * '='
    data = [6,7,8,9,10,11,12]
    df =  pd.Series(data)
    print(df)
    
    print(border)
    
    print("Mean Of dataset is : ")    
    print(df.mean())




if __name__ == "__main__":
    main()