"""
Q4 . Display Students who scored  more than  85 in Science.   

data = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English':[75,85,82]
        }
"""
import pandas as pd


def main():
    border = 50 * '-'
    data = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English':[75,85,82]
        }

    # load to pandas dataframe
    df = pd.DataFrame(data)

    print(border)
    print(df)
    print(border)

    #Shape of dataset
    print("Shape of dataset")
    print(df.shape)
    print(border)

    #Print columns of dataframe
    print("Print columns of dataframe")
    print(df.columns)
    print(border)

    #Data type 
    print("Data type")
    print(df.dtypes)
    print(border)

    print("descriptive statistics")
    print(df.describe())
    print(border)

    print("Add total column")
    df['Total'] = df.sum(axis=1,numeric_only=True)
    print(df)   
    print(border)

    print(" Display Students who scored  more than  85 in Science. ")

    print(df[df['Science'] > 85])
    print(border)
    



    


if __name__ == "__main__":
    main()
