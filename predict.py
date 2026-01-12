import joblib
import numpy as np

model = joblib.load("model/crop_model.pkl")

def recommend_crop(n, p, k, ph, temp, humidity, rainfall):
    data = np.array([[n, p, k, ph, temp, humidity, rainfall]])
    return model.predict(data)[0]
