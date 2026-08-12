"""
Train Three Decision Tree model with
max_depth = 1
max_depth = 3
max_depth = None

Compare theire testing accurecy and write your observation

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



    model = DecisionTreeClassifier(criterion=  'gini', max_depth=1)

    model = model.fit(X_train,Y_train)

    Y_pred = model.predict(X_test)

    accuracy_testing = accuracy_score(Y_test,Y_pred)

    print("testing accurecy  of model on max depth 1 is :",accuracy_testing * 100)


    model = DecisionTreeClassifier(criterion=  'gini', max_depth=3)

    model = model.fit(X_train,Y_train)

    Y_pred = model.predict(X_test)

    accuracy_testing = accuracy_score(Y_test,Y_pred)

    print("testing accurecy  of model on max depth 3 is :",accuracy_testing * 100)

    # In above scenario max depth with values None, 1 and 3 accuracy always gives different value 83.333, 100 percent














    
if __name__ == "__main__":
    main()