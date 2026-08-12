"""
Calculate 
- Training accurecy
- Testing accurecy
Compare both  and comment whether the model is overfitting or underfitting 
"""
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report

    )
import matplotlib.pyplot as plt 
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

    model =DecisionTreeClassifier()

    model= model.fit(X_train,Y_train)

    print("Model training complited")

    Y_pred = model.predict(X_test)

    Y_train_pred = model.predict(X_train)

    accuracy_testing = accuracy_score(Y_test,Y_pred)

    accuracy_training = accuracy_score(Y_train,Y_train_pred)

    print("Training Accuracy of model is :",accuracy_training * 100," %")    #100%

    print("Testing Accurecy of model  is :",accuracy_testing * 100," %")    #100%

    cm = confusion_matrix(Y_test,Y_pred)
    print("Confusion Matrix")
    print(cm)
    data = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=model.classes_)

    data.plot()
    plt.title("Confusion Matrix")
    plt.show()
  
    # Overfitting : An overfit model performs extremely well on the training data but poorly on unseen
    # test data. In our case accuracy is 100% on both training and testing dataset.
    # So our model is not overfit.

    # Underfitting : An underfit model performs poor on both training and testing datasets.
    #our model is not underfit also.

    # Model is good fit ..
    
if __name__ == "__main__":
    main()