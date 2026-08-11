"""
Plot sleep hours  against  FinalResult . Does Sleeping more guarentee success ?Explain
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
    plt.figure(figsize=(8,6))
    sns.scatterplot(data=dataframe, x= "SleepHours", y="FinalResult", hue="FinalResult")
    plt.show()
    SleepHours_corr = dataframe[["SleepHours", "FinalResult"]] # 0.85
    sns.heatmap(data= SleepHours_corr.corr(), annot=True, cmap="coolwarm")
    plt.show()
    #  plot if sleep hours increases chances of getting passed is more.Also
    # correlation is strong in this feature and lable.


    
if __name__ == "__main__":
    main()