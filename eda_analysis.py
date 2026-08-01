import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("dataset.csv")
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.isnull().sum())
print(df.describe())
print("Mean Quantity:", df["Quantity"].mean())
print("Median Quantity:", df["Quantity"].median())
plt.figure(figsize=(8,5))
sns.boxplot(x=df["TotalPrice"])
plt.show()
plt.figure(figsize=(8,5))
sns.histplot(df["TotalPrice"], kde=True)
plt.show()
corr = df.corr(numeric_only=True)

plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True)
plt.show()
df.groupby("Product")["TotalPrice"].sum().sort_values(ascending=False)