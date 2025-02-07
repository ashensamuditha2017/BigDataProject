# Big Data Project: Social Media Engagement & Productivity Analysis

## 📌 Project Overview
This project analyzes video engagement patterns on social media to predict user satisfaction, identify addiction levels, and understand productivity loss. The dataset is stored in **MongoDB Atlas**, processed using **Dask**, analyzed with **Pandas**, visualized using **Matplotlib & Seaborn**, and deployed as a **Streamlit dashboard**.

## 📂 Folder Structure
big_data_project/ 
    │── data/ # Store raw and processed data │ 
        ├── raw_data.csv # Original dataset (if applicable) │ 
            ├── processed_data.parquet/ # Processed Parquet files │ 
        ├── visualizations/ # Saved visualization images 
    │── notebooks/ # Jupyter notebooks for EDA and visualization │ 
        ├── eda.ipynb # Exploratory Data Analysis (Step 3) │ 
        ├── analysis.ipynb # Advanced analysis (Step 4) │ 
        ├── visualization.ipynb # Data visualization (Step 5) 
    │── scripts/ # Python scripts for automation │ 
        ├── step1_upload_mongo.py # Upload raw data to MongoDB Atlas │ 
        ├── step2_process_data.py # Process data using Dask │ 
        ├── step4_analysis.py # Advanced analytics using Pandas & Dask 
    │── cloud/ # Cloud deployment setup │ 
        ├── streamlit_dashboard.py # Streamlit dashboard for visualization 
    │── requirements.txt # Python dependencies 
    │── config.py # Configuration settings (MongoDB URI, etc.) 
    │── README.md # Project documentation & instructions   (this file)

## 🚀 Installation & Setup

### **Step 1: Install Dependencies**
Run the following command to install required Python libraries:
```sh
pip install -r requirements.txt
```

## ***Step 2: Set Up MongoDB Atlas**
Sign up on MongoDB Atlas.
Create a free cluster.
Create a database bigdata_project and collection social_media_analysis.
Copy your MongoDB connection string and store it in config.py.

## ***Step 3: Upload Data to MongoDB**
Run the script to upload the dataset:
```sh
python scripts/step1_upload_mongo.py
```

## ***Step 4: Process Data using Dask**
```sh
python scripts/step2_process_data.py
```

## ***Step 5: Perform Exploratory Data Analysis (EDA)**
Launch Jupyter Notebook:
```sh
jupyter notebook
```
Open the eda.ipynb notebook and execute it.

## ***Step 6: Run Advanced Analytics with Pandas & Dask**
```sh
python scripts/step4_analysis.py
```

## ***Step 7: Generate Visualizations**
Open and run notebooks/visualization.ipynb in Jupyter Notebook.

## ***Step 8: Deploy Dashboard**
Run the Streamlit dashboard:
```sh
streamlit run cloud/streamlit_dashboard.py
```

📊 Features
✔️ MongoDB Atlas for NoSQL storage
✔️ Dask for large-scale data processing
✔️ Pandas for data analysis
✔️ Seaborn & Matplotlib for visualization
✔️ Streamlit for cloud-based interactive dashboard

📌 Dataset
The dataset used in this project is from Kaggle: "Time-Wasters on Social Media".
It contains user behavior, engagement, and addiction-level data across multiple platforms.

💡 Future Improvements
Implement real-time data ingestion using Kafka (optional)
Deploy on AWS/GCP for scalability
Use Machine Learning for predictive analytics