"""
Trainm model with"
- max_depth = None
Calculate
    -Training accuracy 
    - Testing accuracy

If the training accuracy is 100% and testing accuracy is lower. explain why this happen
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
import seaborn as sns
from sklearn.tree import plot_tree

border = "-"*50

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
    global border 
    path = "student_performance_ml.csv"

    ##############################################################
    # Load the Dataset
    ##############################################################
    print(border)
    print("Dataset Loading")
    print(border)


    df = loadDataset(path)

    if df is None:
        print("Please check dataset is exist or not")  
        return

    print("Datset loaded successfully")



    ##############################################################
    # Data Analysis
    ##############################################################
    print(border)
    print("Data Analysis")
    print(border)
    correlation = df.corr()
    print("Correlation between all contiguous features and labels with each other")
    print(correlation)
    print("")
    print("Description of dataset :")
    print(df.describe())

    print("");
    print("Missing values from dataset columns: ")
    print(df.isnull().value_counts())
    
    print("")
    print("Percentage of each labels/dependent variables")
    passed_count = (df["FinalResult"] == 1).sum()
    failed_count = (df["FinalResult"] == 0).sum()
    pass_percen = (passed_count/ (passed_count + failed_count)) * 100
    fail_percen = (failed_count/ (passed_count + failed_count)) * 100

    print(f"Percentage passed students in dataset [1] : {pass_percen}%")       # 60.0 %
    print("Percentage failed students in dataset [0] : %2.f%%" % fail_percen)  # 40.0 %

    ###############################################################
    #   3. Visualization of Dataset
    ###############################################################
    print(border)
    print("3. Visualization of Dataset")
    print(border)

    plt.figure(figsize=(8,6))

    sns.heatmap(data=df.corr(), annot=True)
    plt.title("Correlation of features and labels from the dataset")
    plt.show()

    sns.scatterplot(data=df, x="StudyHours", y="PreviousScore", hue="FinalResult")
    plt.title("Relation between Study Hours and Previous Score")
    plt.show()

    sns.boxplot(x=df["Attendance"])
    plt.title("Outliers values from Attendance column")
    plt.show()

    ###############################################################
    #   4. Train-Test Split of Dataset
    ###############################################################
    print(border)
    print("4. Train-Test Split of Dataset")
    print(border)

    indepedent_variables = ["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]

    X = df[indepedent_variables]
    Y = df["FinalResult"]
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size=0.8, random_state=42)

    print("Train-Test splitting completed...")

    ###############################################################
    #   5. Model Training
    ###############################################################
    print(border)
    print("5. Model Training")
    print(border)

    model = DecisionTreeClassifier(criterion="gini", max_depth=None)

    model = model.fit(X_train, Y_train)

    print("Model Training Completed")

    Y_pred = model.predict(X_test)

    Y_Train_pred = model.predict(X_train)

    accuracy = accuracy_score(Y_train, Y_Train_pred)

    print("Training accuracy with max depth None is ", accuracy*100)


    accuracy = accuracy_score(Y_test, Y_pred)

    print("Testing accuracy with maxdepth None ", accuracy*100)

    #ml model on two completely separate datasets with different roles. 

if __name__ == "__main__":
    main()