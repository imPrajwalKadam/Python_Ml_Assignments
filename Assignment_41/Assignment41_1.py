"""
We Have to design machine learning application which uses classification technique

Design machine learning application which follows below steps as

step 1:
Get Data    

step 2:
Clean ,prepair and manipullate data

step 3:
Train Data
 
step 4:
Test Data

step 5:
Calculate accuracy

"""
import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

#############################################
#Function Name : load_dataset(path)
#Parameter : string
#returnValue : dict
#Author : Prajwal Pradeep Kadam
#Date : 13/08/2026  
#############################################

border = 50 * "-"
def load_dataset(path):
    df = None
    if os.path.exists(path):
        df = pd.read_csv(path)
    return df




def main():

    ##############################################
    #Step 1 : Load the Dataset
    ##############################################

    path = "WinePredictor.csv"
    df = load_dataset(path)
    print(border)
    print("Dataset Loaded Succcessfully ")
    print(border)

    print(df.head())
    print(df.tail())

    print(border)

    ###############################################
    #Step 2 :  Clean ,prepair and manipullate the data
    ###############################################
    print(border)
    print("Stept 2 : Clean The Dataset")
    print(border)
    df.dropna(inplace=True)
    print("Shape of dataset : ",df.shape)
    print("Total rows : ",df.shape[0])
    print("Total columns : ",df.shape[1])
    print(border)

    #seperate dependent and independent variables
    
    #Independent  variables/ Features

    #drops only Class and only other values to X variables because theya are independent\features varible we want this variables in X .

    X = df.drop(columns="Class")

    #dependent Variable / Label  also Target
    #Class is a label set it to Y

    Y = df["Class"]

    print("Shape of X ", X.shape)

    print("Shape of Y ",Y.shape)

    print(border)
    print("Input\Feature Columns : ", X.columns.tolist())
    print("Output\Label\Target Columns : Class")

    #Split The Dataset For training ans testing
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.20,random_state=42,stratify =Y)

    print(border)
    print("Details of training and testing data : ")

    print("Shape of X_train ",X_train.shape)

    print("Shape of X_test ", X_test.shape)

    print("Shape of  Y_train",Y_train.shape )

    print("Shape of Y_test",Y_test.shape)
    print(border)

    #Features scalling  Data manipulation
    scalar = StandardScaler()
    X_train_scaled = scalar.fit_transform(X_train)
    X_test_scaled = scalar.fit_transform(X_test)
    print("Feature Scaling done ")
    print(border)



    ###############################################
    #Step 3 : Build the model Train the model
    ###############################################
    print(border)
    print("Step 3 : Build the model Train the model")
    print(border)

    # Build the model  our dataset is classification dataset so we are using any classification model here we are using KNN  
    model = KNeighborsClassifier(n_neighbors=3)

    print("Classification model is created")

    # Train the model
    model = model.fit(X_train_scaled,Y_train)
    print("Model training completed")
    print(border)


    ################################################
    #Step 4 : Test the model\Data
    ################################################
    print(border)
    print("Step 4 : Test the model")
    print(border)
    Y_pred = model.predict(X_test_scaled)


    ####################################################
    #Step 5 : Calculate Accuracy
    ####################################################
    print(border)
    print("Step 5 : Calculate Accuracy")
    print(border)

    accuracy = accuracy_score(Y_test,Y_pred)
    print("Model Accuracy is :",accuracy*100)

    print(border)
if __name__ == "__main__":
    main()