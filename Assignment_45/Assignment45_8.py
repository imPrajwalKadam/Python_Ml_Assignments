"""

Machine Learning Assignments 
Q8 : Plot a histogram  of math marks.

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

print("Number of student pass :  ",passCnt)

print("Plot a histogram  of math marks.")

# Plotting the Histogram for Math marks
df['Math'].plot.hist(
    bins=[70, 80, 90, 100],  # Defines the grade intervals (70-80, 80-90, 90-100)
    edgecolor='black',       # Adds a clean border between bars
    color='#66b3ff'          # Custom bar color
)

# Customising the labels
plt.title('Distribution of Math Marks')
plt.xlabel('Marks Range')
plt.ylabel('Number of Students')

# Force x-axis to show the exact bin boundaries
plt.xticks([70, 80, 90, 100])

plt.show()