"""
Q1 . Create dataframe  for student marks and print basic  information like shape , columns , and data type
data = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English':[75,85,82]
        }
"""
import pandas as pd


def main():
    data = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English':[75,85,82]
        }

    # load to pandas dataframe
    df = pd.DataFrame(data)

    print(df)
    #Shape of dataset
    print(df.shape)

    #Print columns of dataframe
    print(df.columns)
    #Data type 
    print(df.dtypes)
    


if __name__ == "__main__":
    main()
