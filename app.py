import streamlit as st
from predict import recommend_crop

st.set_page_config(page_title="Crop Recommendation", layout="centered")

st.title(" AI-Based Crop Recommendation System")
st.write("Enter soil and weather details")


##  user enter the input for each field

n = st.number_input("Nitrogen (N)", 0, 140)
p = st.number_input("Phosphorus (P)", 0, 145)
k = st.number_input("Potassium (K)", 0, 210)
ph = st.slider("Soil pH", 0.0, 14.0)    #Slider used because pH is a decimal value
temp = st.slider("Temperature (°C)", 0.0, 50.0)
humidity = st.slider("Humidity (%)", 0.0, 100.0)
rainfall = st.slider("Rainfall (mm)", 0.0, 300.0)

## button creation


if st.button("Recommend Crop"):
    crop = recommend_crop(n, p, k, ph, temp, humidity, rainfall)
    st.success(f" Recommended Crop: {crop}")
