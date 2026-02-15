import pandas as pd
import numpy as np

# Creating a messy dataset that mimics human error
data = {
    'patient_id': [1, 2, 3, 4, 5, 6],
    'age': [25, np.nan, 40, 150, 35, 29],  # Missing value and an impossible age
    'weight_kg': [70, 80, -5, 65, 72, np.nan], # Negative weight and a missing value
    'blood_type': ['A', 'B', 'O', 'Z', 'AB', 'A'], # 'Z' is an invalid blood type
}

df = pd.DataFrame(data)
df.to_csv('raw_hospital_data.csv', index=False)
print("⚠️ Raw 'messy' data generated!")