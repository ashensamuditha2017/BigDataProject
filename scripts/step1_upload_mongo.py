import sys
import os
import pandas as pd
import pymongo

# Add parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import MONGO_URI

# Connect to MongoDB Atlas
client = pymongo.MongoClient(MONGO_URI)
db = client["bigdata_project"]
collection = db["social_media_analysis"]

# Load dataset
df = pd.read_csv("data/time_wasters.csv")  # Update filename if needed

# Convert DataFrame to dictionary and insert into MongoDB
data_dict = df.to_dict(orient="records")
collection.insert_many(data_dict)

print("Data successfully uploaded to MongoDB Atlas!")