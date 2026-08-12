"""
Use the trained model to predict result  for student with :
- Studyhoure = 6
- Attendance = 85
- PreviousScore = 66 
- AssignmentComplited = 7
- SleepHours = 7
Will the student pass or fail ? 
"""



import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt 
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report
    )

##############################################################
#FunctionName : loadDataset(path)
#Parameters : string
#return value : dict
#author Name : Prajwal Preadeep Kadam
#Date : 11/08/2026
##############################################################
def loadDataset(path):
    df = None
    if os.path.exists(path):
        df = pd.read_csv(path)
    return df
    
def main():
    ##############################################################
    # Load the Dataset
    ##############################################################

    path = "student_performance_ml.csv"

    df = loadDataset(path)

    independent_variables = ["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]

    X = df[independent_variables]

    Y = df["FinalResult"]

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    model = DecisionTreeClassifier(criterion=  'gini', max_depth=None)

    model = model.fit(X_train,Y_train)

    Y_pred = model.predict(X_test)

    accuracy_testing = accuracy_score(Y_test,Y_pred)

    print("testing accurecy  of model on max depth None is :",accuracy_testing * 100)

    result = ["Passed","Failed"]
    data = {
        "StudyHours":[6.0],
        "Attendance":[85],
        "PreviousScore":[66],
        "AssignmentsCompleted":[7],
        "SleepHours":[7]
    }

    df_test = pd.DataFrame(data)
    df_pred = model.predict(df_test)
    print(df_pred)
    if df_pred is not None and len(df_pred) > 0:
        print("Prediction result of student is :", result[df_pred[0]])
    else:
        print("Unable to predict the result")


    
if __name__ == "__main__":
    main()