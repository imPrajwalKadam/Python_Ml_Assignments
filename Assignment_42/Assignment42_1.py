"""
Machine Learning Assignment
1. Write Python Program that classifies a new data point using the K-Nearest Neighbors algorethm.
    The Algorithm Should be implimented manualay without using any machine learning library .

    The Program should
    - Calculate Euclidean distance
    - Sort Distances
    - Select K nearest neighbors
    - Predict the class based on major voting

    Dataset :
    Point X Y Label
    A     1 2 red
    B     2 3 red  
    C     3 1 blue
    D     6 5 blue

    Tasks:
        1 . Accept X And Y cordinates of a new point from the user
        2. Compute Euclidean distance from all dataset points
        3. sort the distance 
        4. Select K = 3 nearest neighbors
        5. Predict the class labels

    Input Format
        Enter X coordinate : 2
        Enter Y coordinate : 2

    Expected output

    Nearest Neighbors : 
        A - Distance: 1.0
        B - Distance: 1.0
        B - Distance: 1.41

    Predicted Class = red
"""
import numpy as np
import math
border = "-" *50

def EucilideanDistance(P1,P2):
    ans = math.sqrt((P1['X'] - P2['X'])**2 + (P1['Y'] - P2['Y'])**2)
    return ans


def CustomKnnClassifier(X,Y,k=3):
    Data = [
        {'Points':'A', 'X':1,'Y':2,'label':'Red'},
        {'Points':'B', 'X':2,'Y':3,'label':'Red'},
        {'Points':'C', 'X':3,'Y':1,'label':'Blue'},
        {'Points':'D', 'X':6,'Y':5,'label':'Blue'}
    ]
    print((border))
    print("Custom KNN Classifier")
    print(border)

    for i in Data:
        print(i)
    print(border)
    new_point = {"X":X,"Y":Y}
    print("Distence of all points :")
    print(border)
    for d in Data:
        d["distance"] = EucilideanDistance(d,new_point)

    for d in Data:
        print(d)

    print(border)

    sorted_data = sorted(Data,key = lambda item:item["distance"])

    print(border)
    print("Sorted data")
    print(border)

    for d in sorted_data:
        print(d)

    print(border)

    nearest = sorted_data[:k]
    print(border)
    print("Nearest 3 members are ")
    print(border)
    for d in nearest:
        print(d)
def main():
    X = int(input("Enter X Coordinates :"))
    Y = int(input("Enter Y Coordinates :"))
    CustomKnnClassifier(X,Y)


if __name__ == "__main__":
    main()