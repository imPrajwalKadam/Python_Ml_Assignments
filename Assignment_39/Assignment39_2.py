"""
Use the trained model to predict result for X_test . Display Predected values alsong with actual values
"""
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

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
    # Load Dataset
    ##############################################################

    path = "student_performance_ml.csv"
    df = loadDataset(path)

    independent_variables = ["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]
    X = df[independent_variables]
    Y = df["FinalResult"]
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
    model =DecisionTreeClassifier()
    model= model.fit(X_train,Y_train)
    print("Model training complited")
    Y_pred = model.predict(X_test)
    print("Actual value :")
    print(Y_test)
    print("Predicted value : ")
    print(Y_pred)


if __name__ == "__main__":
    main()