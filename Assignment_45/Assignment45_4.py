"""
Machine Learning Assignments 
Q4 : Plot a pie chart of subject marks of Sagar
"""
import pandas as pd
import matplotlib.pyplot as plt

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

sagarMarks = df[df['Name'] == 'Sagar'].drop(columns = ['Name','Gender']).squeeze()
sagarMarks.plot.pie(
    autopct='%1.1f%%', 
    startangle=90, 
    colors=['#ff9999','#66b3ff','#99ff99']
)

plt.title("Sagar marks ")
plt.show()