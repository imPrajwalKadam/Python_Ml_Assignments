"""
Draw box plot for attendance .
Identify  if any outliers are present
"""
import pandas as pd
import seaborn as sns
import os
import matplotlib.pyplot as plt

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

    # Draw a single box plot
    dataFrame.boxplot(column='Attendance')

    plt.show()


    
if __name__ == "__main__":
    main()