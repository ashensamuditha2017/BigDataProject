import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns

# Updated path for the image
visualization_path = r"D:\Ashen Samuditha\Pictures\BigData\engagement_vs_addiction.png"

# Load the processed data
file_path = os.path.join("data", "processed_data.parquet")
df = pd.read_parquet(file_path)

# Streamlit Dashboard Content
st.title("Big Data Analytics Dashboard - (Social Media Engagement Analysis)")

# Display Top Engaged Users
st.subheader("Top Engaged Users")
st.write(df.nlargest(5, "Engagement"))

# Engagement vs Addiction Level Scatter Plot
st.subheader("Engagement vs Addiction Level")
st.scatter_chart(df[["Engagement", "Addiction Level"]])

# Add dropdown filters
platform = st.selectbox('Select Platform:', df['Platform'].unique())
filtered_df = df[df['Platform'] == platform]

# Show Summary Statistics
st.write("### Summary Statistics")
st.write(filtered_df.describe())

# Display Visualizations
st.subheader("📌 Engagement vs Productivity Loss")
visualization_path_EPL = r"D:\Ashen Samuditha\Pictures\BigData\engagement_vs_productivity.png"
st.image(visualization_path_EPL)

st.subheader("📌 Time-Series Analysis: Engagement Trends")
visualization_path_TSET = r"D:\Ashen Samuditha\Pictures\BigData\engagement_trend.png"
st.image(visualization_path_TSET)

st.subheader("📌 User Behavior Clustering")
visualization_path_UBC = r"D:\Ashen Samuditha\Pictures\BigData\user_clusters.png"
st.image(visualization_path_UBC)

st.subheader("📌 Addiction Level by Demographics")
visualization_path_ALD = r"D:\Ashen Samuditha\Pictures\BigData\addiction_demographics.png"
st.image(visualization_path_ALD)

st.subheader("📌 Engagement Based by Platform")
visualization_path_EBP = r"D:\Ashen Samuditha\Pictures\BigData\engagement_by_platform.png"
st.image(visualization_path_EBP)

# Check if the image file exists and display it
if os.path.exists(visualization_path):
    st.subheader("📌 Engagement vs Addiction Level")
    st.image(visualization_path)  # Pass the path directly
else:
    st.error(f"Visualization file not found at {visualization_path}. Please ensure the file exists.")

st.write("#### Data Source: [Kaggle Dataset](https://www.kaggle.com/datasets/zeesolver/dark-web)")