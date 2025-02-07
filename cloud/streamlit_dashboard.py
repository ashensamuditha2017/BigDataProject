import streamlit as st
import pandas as pd
import os

# Updated path for the image
visualization_path = r"D:\Ashen Samuditha\Pictures\BigData\engagement_vs_addiction.png"

# Load the processed data
file_path = os.path.join("data", "processed_data.parquet")
df = pd.read_parquet(file_path)

# Streamlit Dashboard Content
st.title("Big Data Analytics Dashboard")

# Display Top Engaged Users
st.subheader("Top Engaged Users")
st.write(df.nlargest(5, "Engagement"))

# Engagement vs Addiction Level Scatter Plot
st.subheader("Engagement vs Addiction Level")
st.scatter_chart(df[["Engagement", "Addiction Level"]])

# Check if the image file exists and display it
if os.path.exists(visualization_path):
    st.subheader("Visualization")
    st.image(visualization_path)  # Pass the path directly
else:
    st.error(f"Visualization file not found at {visualization_path}. Please ensure the file exists.")
