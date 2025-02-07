import os
import dask.dataframe as dd

# Corrected project root path
file_path = os.path.join("data", "processed_data.parquet")

# Print the file path for debugging
print(f"File path: {file_path}")

# Load processed data with Dask (read parquet file)
df = dd.read_parquet(file_path)

# Example Analysis: Find top 5 most engaged users
top_users = df.groupby("UserID")["Engagement"].sum().nlargest(5)

# Display the result (compute the result)
print(top_users.compute())

print("✅ Advanced analytics completed!")
