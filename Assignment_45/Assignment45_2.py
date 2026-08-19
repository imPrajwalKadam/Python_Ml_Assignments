"""
Machine Learning Assignments 
Q2 : Create a gender column and perform one-hot encoding. 
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
print("Fataframe encoded for gender column ")
encoded_df = pd.get_dummies(df,columns=['Gender'],dtype=int)

print(encoded_df)

print(border)