import pandas as pd
import matplotlib.pyplot as plt

# ==========================
# Step 1: Load Raw Dataset
# ==========================
df = pd.read_csv("sanjay.CSV")

print("Original Dataset")
print(df.head())

# ==========================
# Step 2: Check Dataset
# ==========================

print(df.info())
print(df.shape)

# Missing Values
print(df.isnull().sum())

# Duplicate Records
print("Duplicates :", df.duplicated().sum())

# ==========================
# Step 3: Data Cleaning
# ==========================

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing Salary with mean
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# Fill missing City
df["City"] = df["City"].fillna("Unknown")

# Remove rows where Sales is missing
df = df.dropna(subset=["Sales"])

# Convert datatype
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

print("Cleaning Completed")

# ==========================
# Step 4: Save Clean Dataset
# ==========================

df.to_csv("Cleaned_Sales_Data.csv", index=False)

print("Cleaned CSV Saved Successfully")

top10 = df.sort_values(by="Sales", ascending=False).head(10)

print(top10[["Customer_ID","Sales"]])

plt.figure(figsize=(10,5))
plt.bar(top10["Customer_ID"].astype(str), top10["Sales"])
plt.title("Top 10 Sales")
plt.xlabel("Customer ID")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
