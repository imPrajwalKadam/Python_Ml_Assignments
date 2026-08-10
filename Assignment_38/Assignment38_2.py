"""
Write a program to :
-  Display total number of student in the dataset
-  Count how many students Passed (FinalResult= 1)
-  Count how many students failed (final result= 0)
"""

import pandas as pd
path = "student_performance_ml.csv"
df = pd.read_csv(path)
print("Dataset loaded successfully")


print("Total number of student in the dataset")
print(len(df))

print("How many student passed ?")
countpass = len(df[df["FinalResult"] ==1])
print("Answer ->",countpass)

print("How many student fail ?")
countFail = len(df[df["FinalResult"] == 0])
print("Asnwer ->",countFail)



