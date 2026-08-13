"""
2. The value of k plays an importent roll in KNNalgorithm
Write a python program that demonstrates how  prediction changes when K changes

Dataset
use the same dataset as assignment 1.

predict the class of the same new point using:
- K = 1
- K = 3
- K = 5

Expected output
Prediction result
K = 1 -> Red
K = 3 -> Red
K = 5 -> Blue

Explain why the prediction change when k incress
 
"""
import numpy as np
import math

border = "-" *50

def EucilideanDistance(P1,P2):
    ans = math.sqrt((P1['X'] - P2['X'])**2 + (P1['Y'] - P2['Y'])**2)
    return ans

def Predict_label(sorted_distence,k):
    global border
    sorted_distence_k = sorted_distence[:k]
    votes = {}
    print(sorted_distence_k)

    for d in sorted_distence_k:
        label = d["label"]
        votes[label] = votes.get(label, 0) + 1

    print(border)
    print(f"Predicted class label with value K {k}")
    print(border)
    
    y_pred = max(votes, key=votes.get)
    print(y_pred)
    print(border)


def CustomKnnClassifier(X,Y,k=5):
    global border 
    Data = [
        {'Points':'A', 'X':1,'Y':2,'label':'Red'},
        {'Points':'B', 'X':2,'Y':3,'label':'Red'},
        {'Points':'C', 'X':3,'Y':1,'label':'Blue'},
        {'Points':'D', 'X':5,'Y':6,'label':'Blue'}
    ]
    print((border))
    print("Custom KNN Classifier")
    print(border)

    new_point = {"X":X,"Y":Y}
    for d in Data:
        d["distance"] = EucilideanDistance(d,new_point)

    sorted_data = sorted(Data,key = lambda item:item["distance"])
    Predict_label(sorted_data,1)
    Predict_label(sorted_data,3)
    Predict_label(sorted_data,5)

def main():
    X = int(input("Enter X Coordinates :"))
    Y = int(input("Enter Y Coordinates :"))
    CustomKnnClassifier(X,Y)


if __name__ == "__main__":
    main()