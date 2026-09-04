import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)
from sklearn.datasets import load_breast_cancer


# ---------------------------------------
# Step 1 : Load the dataset
# ---------------------------------------

df = load_breast_cancer()

# Convert sklearn dataset into DataFrame
X = pd.DataFrame(df.data, columns=df.feature_names)
Y = pd.Series(df.target)

print("Dataset Shape :", X.shape)
print("Target Shape  :", Y.shape)

print("\nFirst 5 records:")
print(X.head())

print("\nTarget values:")
print(Y.value_counts())


# ---------------------------------------
# Step 2 : Check missing values
# ---------------------------------------

print("\nMissing values:")
print(X.isnull().sum().sum())


# ---------------------------------------
# Step 3 : Summary statistics
# ---------------------------------------

print("\nSummary Statistics:")
print(X.describe())


# ---------------------------------------
# Step 4 : Split dataset
# ---------------------------------------

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42,
    stratify=Y
)

print("Training data shape :", X_train.shape)
print("Testing data shape  :", X_test.shape)


# ---------------------------------------
# Step 5 : Scale the features
# ---------------------------------------

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# ---------------------------------------
# Step 6 : Create the model
# ---------------------------------------

model = DecisionTreeClassifier(random_state=42)


# ---------------------------------------
# Step 7 : Train the model
# ---------------------------------------

model.fit(X_train, Y_train)


# ---------------------------------------
# Step 8 : Make predictions
# ---------------------------------------

Y_pred = model.predict(X_test)


# ---------------------------------------
# Step 9 : Evaluate the model
# ---------------------------------------

accuracy = accuracy_score(Y_test, Y_pred)

print("\n========== MODEL EVALUATION ==========")

print("Accuracy :", accuracy)

print("\nConfusion Matrix:")
print(confusion_matrix(Y_test, Y_pred))

print("\nClassification Report:")
print(classification_report(
    Y_test,
    Y_pred,
    target_names=["Malignant", "Benign"]
))

