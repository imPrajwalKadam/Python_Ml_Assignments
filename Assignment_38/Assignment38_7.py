"""
Create scatter plot of studyHoure vs PreviousScore
Use different color for pass and fail students
"""
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
border = "-" *50


def load_dataset_csv(path):
    print(path)
    datframe = None
    if os.path.exists(path):
        datframe = pd.read_csv(path)
    return datframe

def main():
    global border
    ######################################################
    #Load DataSet
    #######################################################

    data_path = "student_performance_ml.csv"

    dataFrame = load_dataset_csv(data_path) 
    if dataFrame is None:
        print("Data Frame is none please provide valid file path")
        return

    # plt.figure(figsize=(8,6))
    # sns.histplot(data=list(dataFrame['StudyHours']))

    study_hours = dataFrame["StudyHours"]
    previousScore = dataFrame["PreviousScore"]
    colors = np.where(dataFrame["FinalResult"]== 1,'green','red')
    plt.scatter(
        study_hours,
        previousScore,
        s = 100,
        marker="o",
        alpha=0.8,
        edgecolors="black",
        linewidths=1,
        label = "Students"
    )
    
    plt.title("Study houre of student")
    plt.xlabel("Study Hours")
    plt.ylabel("previous Marks")
    plt.scatter(dataFrame["FinalResult"],previousScore ,c=colors)

    plt.grid(True)
    plt.legend()
    plt.show()


    
if __name__ == "__main__":
    main()