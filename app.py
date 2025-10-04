# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 20:39:59 2025

@author: user
"""
import os
import pickle
import pandas as pd
import streamlit as st

# Get path of model file relative to app.py
model_path = os.path.join(os.path.dirname(__file__), "phone_sales_data.sav")

# Load the trained model
with open(model_path, "rb") as file:
    loaded_model = pickle.load(file)

# Function to predict phone price
def phone_price_prediction(screen_size, ram, storage, battery_capacity, camera_quality):
    new_phone = pd.DataFrame([{
        'Screen Size (inches)': screen_size,
        'RAM (GB)': ram,
        'Storage (GB)': storage,
        'Battery Capacity (mAh)': battery_capacity,
        'Camera Quality (MP)': camera_quality
    }])
    predicted_price = loaded_model.predict(new_phone)
    return predicted_price[0]

# Main Streamlit app
def main():
    st.set_page_config(page_title="Phone Price Predictor", page_icon="📱", layout="centered")
    st.title("📱 Phone Price Prediction App")
    st.write("Enter phone specifications to predict its price.")

    # Input fields
    screen_size = st.text_input('Screen Size (inches)', '6.2')
    ram = st.text_input('RAM (GB)', '4')
    storage = st.text_input('Storage (GB)', '64')
    battery_capacity = st.text_input('Battery Capacity (mAh)', '4000')
    camera_quality = st.text_input('Camera Quality (MP)', '48')

    if st.button('🔮 Predict Price'):
        try:
            # Convert inputs
            screen_size = float(screen_size)
            ram = int(ram)
            storage = int(storage)
            battery_capacity = int(battery_capacity)
            camera_quality = int(camera_quality)

            # Prediction
            price = phone_price_prediction(screen_size, ram, storage, battery_capacity, camera_quality)
            st.success(f"💰 Predicted Phone Price: **${price:.2f}**")
        except Exception as e:
            st.error(f"⚠️ Error: {str(e)}. Please enter valid numeric values.")

if __name__ == "__main__":
    main()