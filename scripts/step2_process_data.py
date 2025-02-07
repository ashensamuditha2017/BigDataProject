import dask.dataframe as dd
import pandas as pd
from pymongo import MongoClient

# MongoDB Atlas URI
mongo_uri = "mongodb+srv://ashensamuditha:1234@cluster0.baprhio.mongodb.net/"
client = MongoClient(mongo_uri)

# Connect to the database and collection
db = client["bigdata_project"]
collection = db["social_media_analysis"]

# Convert MongoDB data to Pandas DataFrame
data = pd.DataFrame(list(collection.find()))

# Convert Pandas DataFrame to Dask DataFrame
df = dd.from_pandas(data, npartitions=4)

print("✅ Data Loaded Successfully into Dask!")


# Drop missing values
df = df.dropna()

# Convert columns to appropriate data types
df["Total Time Spent"] = df["Total Time Spent"].astype(float)
df["Addiction Level"] = df["Addiction Level"].astype(int)

print("✅ Data Cleaning Complete!")

# Save to Parquet format for further processing
df.to_parquet("data/processed_data.parquet", engine="pyarrow", write_index=False)

print("✅ Processed Data Saved Successfully!")