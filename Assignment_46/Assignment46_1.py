import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score



    
def main():
    Border =  "-"*50
    #Step 1 : Load the data

    print(Border)
    print("Load the data")
    print(Border)

    df = pd.read_csv("Advertising.csv")
    print(df.head())
    # Step 2 : Clean prepair and manipulate the data

    print(Border)
    print("Step 2 : Remove unwanted columns")
    print(Border)

    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    print(df.head())
    print(Border)
    print("Step 3 : Check missing values")
    print(Border)

    print("Total missing values : ")
    print(Border)
    print(df.isnull().sum())
    print(Border)
    #seperate dependent and dependent variables
    X = df[['TV','radio','newspaper']]
    Y = df['sales']

    print("Independent variables : ")
    print(X.head())

    print("Dependent variables : ")
    print(Y.head())

    print(Border)

  
    #Split the dataset
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    print("X Training Data : ",X_train.shape)

    print("X Testing Data : ",X_test.shape)


    print("Y Training Data Dependent variables : ", Y_train.shape)

    print("Y Testing Data Dependent variables : " , Y_test.shape)

    print(Border)

    

    #Step 3 : Train the data Create model 
    model = LinearRegression()
    model = model.fit(X_train,Y_train)
    print("Model training successfully")


    #Step 4 Test The model

    print("Test The model")
    y_pred = model.predict(X_test)
    print("Expected  answer ")
    print(y_pred[:3])


    MSE = mean_squared_error(Y_test,y_pred)
    RMSE = np.sqrt(MSE)
    R2 = r2_score(Y_test,y_pred)

    print("MSE : ",MSE)
    print("RMSE : ",RMSE)
    print("R2 :",R2)
    print("TV coefficient : ",model.coef_[0])
    print("Radio coefficient : ",model.coef_[1])
    print("Newspaper coefficient : ",model.coef_[2])
    print("Intercepr : ", model.intercept_)


if __name__ == "__main__":
    main()