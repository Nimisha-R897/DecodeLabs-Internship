import pandas as pd

df = pd.read_csv("dataset.csv")

print(df.head())
import numpy as np
import pandas as pd

# 1. Load dataset
df = pd.read_csv("dataset.csv")

# 2. Display initial status
print("Original Data:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# 3. Remove duplicate rows
df = df.drop_duplicates()

# 4. Fill missing numerical values with column mean
num_cols = df.select_dtypes(include=np.number).columns
if not num_cols.empty:
    df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

# 5. Fill missing categorical values with column mode
cat_cols = df.select_dtypes(include="object").columns
for col in cat_cols:
    mode_val = df[col].mode()
    if not mode_val.empty:
        df[col] = df[col].fillna(mode_val[0])
    
    # Trim extra whitespace around text
    df[col] = df[col].astype(str).str.strip()

# 6. Display results after cleaning
print("\nCleaned Data:")
print(df.head())

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# 7. Save cleaned dataset
df.to_csv("cleaned_dataset.csv", index=False)
print("\nData cleaning complete! Saved to 'cleaned_dataset.csv'.")