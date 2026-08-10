"""
based on the dataset value, analyze whether:
- Higher studyHours incress the chance of passing.
- Higher Attendance improves FinalResult.
    Write your observations in 4 to 5 lines
"""
import pandas as pd

path = "student_performance_ml.csv"
df = pd.read_csv(path)

#calculate average of each pass and fail
minStudyHrs = df.groupby('FinalResult')["StudyHours"].mean()
print(minStudyHrs)


df['hours_bracket']= pd.cut(df["StudyHours"],
                            bins = [0,3,6,df['StudyHours'].max()],labels = ['low (0-3)','Medium (3-6)','High (6+)'])
passingRate = df.groupby('hours_bracket')['FinalResult'].mean() * 100
border = "-"*80
print(border)
print("-------------------Higher study Hours incress the chance of passing--------------")
print(border)
print(passingRate)
print(border)
print("in above codes output  is showing \n0-3 hourse study hours  low chance to pass \n" \
"3-6 hours study incress chance of passing by 66.67 percent  \n"
"if we study 6 hours + chance of passing is 100 percent ")


df['attendance_bracket']= pd.cut(df["Attendance"],
                            bins = [0,50,75,df['Attendance'].max()],labels = ['low (<50%)','Medium (50-75%)','High (>75%)'])

pivote_analyses= df.pivot_table(index="attendance_bracket",columns="hours_bracket",
                                values="FinalResult",aggfunc='mean')*100

passRate = df.groupby('attendance_bracket')['FinalResult'].mean()*100
print(border)
print("-------------------pivote_analyses.--------------")

print(border)
print(passRate)
print(border)

