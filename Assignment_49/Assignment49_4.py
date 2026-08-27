import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# 1. Initialize your dataset
data = [
    [25, 2000],
    [30, 40000],
    [35, 80000]
]
df = pd.DataFrame(data, columns=['Age', 'Salary'])

# 2. Scale the data using StandardScaler
scaler = StandardScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

# 3. Extract the first two points (Row 0 and Row 1)
# Before scaling
p1_before = df.iloc[0].to_numpy()
p2_before = df.iloc[1].to_numpy()

# After scaling
p1_after = df_scaled.iloc[0].to_numpy()
p2_after = df_scaled.iloc[1].to_numpy()

# 4. Calculate Euclidean Distances using numpy's linear algebra module
distance_before = np.linalg.norm(p1_before - p2_before)
distance_after = np.linalg.norm(p1_after - p2_after)

# 5. Output results
print("=== Distance Comparison ===")
print(f"Euclidean Distance BEFORE scaling: {distance_before:,.4f}")
print(f"Euclidean Distance AFTER scaling:  {distance_after:.4f}")
