"""
Write a python program to load the file student_performance_ml.csv using pandas.
Display :
    First five records
    Last five records
    Total number of row and columns
    List of column names
    Datatypes of each column
"""

import pandas as pd
datapath = "student_performance_ml.csv"
df= pd.read_csv(datapath)
print("Dataset loaded successfully ")
print("initial 5 entrys of dataset are :")
print(df.head())

print("Last 5 entrys of dataset are :")

print(df.tail())


print("total number of column and rows :")
print(df.shape)

print("List of column names :",list(df.columns))


print("Data type of each columns : ")
print(df.dtypes)