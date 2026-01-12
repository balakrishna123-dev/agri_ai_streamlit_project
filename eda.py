import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\\Users\\balak\\Downloads\\Crop_recommendation (1).csv")

print(df.head())
print(df.info())
print(df.describe())

# Missing values
print(df.isnull().sum())

# Target distribution
df["crop"].value_counts().plot(kind="bar", title="Crop Distribution")
plt.show()

# Feature distributions
df.hist(figsize=(10,8))
plt.show()

# Correlation heatmap
plt.figure(figsize=(8,5))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.show()
