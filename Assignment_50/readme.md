"""
- Brest Cancer Prediction
Breast Cancer is the one of the leading causes of death among women worldwide.Early detection and accurate diagnosis
play a critical role in increasing survival rates.

You are given a dataset containing various medical features extracted from breast cancer biopsy images.
Your task is to develope machine learning model that can accurately   predict whether a tumor is malignant(harmful)
or benign(non-harmful) based on the given features

- Dataset details
Source :Brest Cancer Wisconsin Dataset 
Number of records :959
Number of features : 30(real-valued features)

Note : Use load_breast_cancer()  method from sklearn to load the dataset 

Features :
- Mean Radius
- Mean Texture
- Mean Perimeter
- Mean Area
- Mean Smoothness
- Mean Compactness
- Mean Concavity
- Mean Symmetry
- Worst Radius , Worst Texture,....(And Other Statucal Measurement)

Target Variable:
0 -> Malignant
1 -> Benign


- Objectives
1. Load and explore the datasets 
2. Perform dataprocessing steps.
    - Handel missing values
    - Normalize or Scale features
3. Perform exploratory data analysis(EDA)
    - Summery statistics
    - Visualization of feature correlations
4. Split the dataset into training and testing sets .
5. Build the machine learning classification model to predict tumor type.
6. Evaluate the model using:
    - Accuracy
    - Confusion matrix
    - Precision ,Recall,F1-Score
7. Provide Your Observation and conclusions.

- Expected Deliverables
Code File:
    - Data Loading
    - Preprocessing
    - Model building
"""