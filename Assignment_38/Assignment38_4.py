"""
Use value_counts() to analyze the distribution of final result. Calculate the percentage of Pass and fail students.
Is the dataset balanced ? justify your answer

dataset is not balanced Pass Students are 60% and fail students are 40%
"""
import pandas as pd

df = pd.read_csv("student_performance_ml.csv")
print("Dataset loaded successfully")


print("Distribution of final result : ")
print(df["FinalResult"].value_counts()) 

PassFailPercentage = df["FinalResult"].value_counts(normalize=True) * 100

print("percentage of Pass and fail students : ")
print(PassFailPercentage)