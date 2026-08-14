There is one dataset of whether conditions.
that dataset contains information as wether and we have to decides whetherr to play or not .
Dataset contains the targeted variables as play which indecates whether to play or not

consider below Marvellous infosystems Play predictor dataset as
"MarvellousInfosystems_PlayPredictor.csv"

- According to dataset there are two features as
    1. Wether 
    2. Temperature
-We have two labels as 
    1. Yes
    2. No

- there are three types of different entries under whether as 
    1. Sunny
    2. Overcast
    3. Rainy

- There are three types of different entries under temreture as 
    1. Hot
    2. Cold
    3. Mild

We have to use Machine learning application which use classification technique
1. Get Data
2. Clean Prepair and Manipulate dadta 
3. Train Model
4. Test Data
5. Improve

- Design Machine learning application which follows below steps as 

Step 1:
    Get Data

    get data from MarvellousInfosystems_PlayPredictor.csv file into python application.

Step 2:
    Clean Prepair and manipulate data 
    As we want to use the above data into machine learning application we have prepare that in the format which is accepted by the algorithms. As our dataset contains two features as Wether and   Temperature . We have to replace each string field into numeric constents by using LabelEncoder from processing module of sklearn .


Step 3:
    Train Data
    Now we want to train our data for that we have to select machine learning algorithm . For that we select K nearest Neighbour algorithm.
    use fit method for training Purpose. for training use whole dataset 


Step 4 :
    test data
    After Successfull training now we can test our trained data by passing some value of whether and temperature .
    as we are using KNN  algorithm use value of k as 3.
    After providing the values check the result and display on screen 

Step 5:
    Calculate Accuracy
    Write one function as checkAccuracy() which calculate accuracy of our algorithm.
    For calculating the accuracy divide the dataset into two equal parts as Training Data and Testing Data
    Calculate Accuracy by changing value of K.
       

