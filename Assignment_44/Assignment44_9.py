"""
Q8 Create a dataframe  with missing values and fill  them with  column mean 
data2 = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[np,nae,76,88],
        'Science':[91,np.nan,85],
        }
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def main():
    border = 50 * '-'
    
    data = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[np.nan,76,88],
        'Science':[91,np.nan,85],
        }

    # load to pandas dataframe
    df = pd.DataFrame(data)

    print(border)
    print(df)
    print(border)

    print("Dataframe after None columns fill to Average of marks")
    numCol = df.select_dtypes(include=['number']).columns

    df[numCol] =  df[numCol].fillna(df[numCol].mean())
    
    print(df)    



if __name__ == "__main__":
    main()
