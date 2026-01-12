# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Sample CSV: crops.csv
df = pd.read_csv("C:\\Users\\balak\\Downloads\\data\\crop-recommendation\\data\\Crop_recommendation.csv")

X = df[['N','P','K','temperature','humidity','ph','rainfall']]
y = df['crop']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

joblib.dump(model, "model.pkl")
print("Model saved!")
