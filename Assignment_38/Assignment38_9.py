"""
Create a plot showing relationship between AssignmentsComplited and final result  . Explain your observation  
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

    dataframe = load_dataset_csv(data_path) 
    assignment_completed_corr = dataframe[["AssignmentsCompleted", "FinalResult"]]
    plt.figure(figsize=(8,6))
    sns.heatmap(data= assignment_completed_corr.corr(), annot=True, cmap="coolwarm")
    plt.show()
    # Correlation is around 0.84 which indicates strong relationship between
    # feature and label . This means that feature value increases, target label tends
    # to increase consistently 


    
if __name__ == "__main__":
    main()