"""
Machine Learning Assignments 
Q1 : Normalize the 'Math' scores using Min-Max Scalling. 
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
mathCol = df['Math']
print(mathCol)


maxMathCore = mathCol.max()
minScore = mathCol.min()


print("Max :",maxMathCore)
print("Min :",minScore)
df['normalized_score'] = (df['Math'] - minScore) / (maxMathCore - df['Math'].min())

print(df)
print(border)