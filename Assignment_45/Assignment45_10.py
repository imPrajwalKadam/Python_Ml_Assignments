"""

Machine Learning Assignments 
Q.10 : Ploat a boxblot for english marks to check distribution    and autliers

"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

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
total_marks = df[['Math', 'Science', 'English']].sum(axis=1)
df['Status'] = np.where(total_marks >= 250, 'Pass', 'Fail')

passCnt = (df['Status'] == 'Pass').sum()

print(df)
print(border)


df['English'].plot.box(
    patch_artist=True,  # Allows filling the box with color
    boxprops=dict(facecolor='#99ff99', color='black')  # Custom color
)


plt.title('Distribution and Outliers of English Marks')
plt.ylabel('Marks')

plt.show()