"""
Identify Students where :
Y_test != Y_Pred
-Display Those rows
- How manny students  were misclassified?
- What common factor do you observe?


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
    border = "-"*50
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

    model = DecisionTreeClassifier(criterion="gini", max_depth=3)

    model = model.fit(X_train, Y_train)
    Y_pred = model.predict(X_test)
    accuracy = accuracy_score(Y_test,Y_pred)
    print("Testing accuracy from sklearn library : ",accuracy *100)
    pred = [0, 1, 1, 0, 1]
    dict_list = [
        {
            "StudyHours" : 3.0,
            "Attendance" : 70,
            "PreviousScore" : 50,
            "AssignmentsCompleted" : 4,
            "SleepHours" : 6
        },
        {
            "StudyHours" : 6.0,
            "Attendance" : 80,
            "PreviousScore" : 60,
            "AssignmentsCompleted" : 8,
            "SleepHours" : 8
        },
        {
            "StudyHours" : 7.0,
            "Attendance" : 65,
            "PreviousScore" : 70,
            "AssignmentsCompleted" : 7,
            "SleepHours" : 7
        },
        {
            "StudyHours" : 2.0,
            "Attendance" : 75,
            "PreviousScore" : 45,
            "AssignmentsCompleted" : 8,
            "SleepHours" : 8
        },
        {
            "StudyHours" : 8.0,
            "Attendance" : 85,
            "PreviousScore" : 80,
            "AssignmentsCompleted" : 8,
            "SleepHours" : 8
        }
    ]
    new_dataframe = pd.DataFrame(dict_list)
    df_pred = model.predict(new_dataframe)

    print("Study Hours\t|\tAttendance\t|\tPrevious Score\t|\tAssignments Completed\t|\tSleep Hours\t|\tFinalResult")
    index = 0
    for new_df in dict_list:
        if pred[index] != df_pred[index]:
            print(new_df["StudyHours"], "\t\t|\t\t", new_df["Attendance"], "\t|\t", new_df["PreviousScore"],
            "\t\t|\t\t", new_df["AssignmentsCompleted"], "\t\t|\t\t", new_df["SleepHours"], "\t|\t", df_pred[index])
            index += 1 
    

if __name__ == "__main__":
    main()