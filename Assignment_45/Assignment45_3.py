"""
Machine Learning Assignments 
Q3 : Group Student by  gender and calculate average marks. 
"""
import pandas as pd
border= "-"*50
data = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English':[75,85,82]
        }

df = pd.DataFrame(data)
print(df)

print(border)

df["Gender"] = ['Male','Male','Female']

print(df)

print(border)
print("Group Student by  gender and calculate average marks.")
Avgdf = df.groupby('Gender')[['Math','Science','English']].mean()
print(Avgdf)