"""
Write a python program using standardscaler to perform feature scalling on 
that following dataset 
[
    [25,2000],
    [30,40000],
    [35,80000]
]
print the scalled dataset.
"""


import pandas as pd
from sklearn.preprocessing import StandardScaler


def main():
    
    
    border = '-'*50
    data = [
        [25,2000],
        [30,40000],
        [35,80000]
        ]
    
    df = pd.DataFrame(data,columns=['Age','Salary'])
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)
    df_scaled = pd.DataFrame(scaled_data,columns=df.columns)
    print(border)
    print("Pandas Original Dataframe ")
    print(df)
    
    print(border)
    print("Scaled  dataframe")
    print(scaled_data)    
    print(border)
    
    


if __name__ == "__main__":
    main()