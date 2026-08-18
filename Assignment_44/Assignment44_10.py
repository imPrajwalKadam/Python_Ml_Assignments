"""
Q10. Drop the englih columns from original dataframe 

data = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English':[75,85,82]
        }
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
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

    print("Drop English column")
    print(df.drop(columns = ['English']))


if __name__ == "__main__":
    main()
