"""
3 .Using pandas  function , calculate and display:
 - Average StudyHours
 - Average Attendance
 - Maximum previousScore
 - Minimum sleepHours
"""

import pandas as pd

df = pd.read_csv("student_performance_ml.csv")
print("Dataset loaded successfully")
print("Average Study hours  : ",df["StudyHours"].mean())
print("Average Attandance  : ",df["Attendance"].mean())
print("Maximum Previous score  : ",df["PreviousScore"].max())
print("Minimum Sleep Hours  : ",df["SleepHours"].min())