
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Step 1: Read the CSV file
file_name = "marketing_campaign.csv"

if not os.path.exists(file_name):
    print("Error: marketing_campaign.csv file not found!")
    print("Place the CSV file in the same folder as this Python program.")
    exit()

# Automatically detect comma or semicolon separator
df = pd.read_csv(file_name, sep=None, engine="python")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Step 2: Display dataset information
print("\nFirst 5 Records:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

# Step 3: Convert required columns to numeric if available
required_columns = [
    "Income",
    "MntWines",
    "MntFruits",
    "MntMeatProducts",
    "MntFishProducts",
    "MntSweetProducts",
    "MntGoldProds"
]

# Check whether all required columns exist
missing_columns = [
    col for col in required_columns if col not in df.columns
]

if missing_columns:
    print("\nRequired columns are missing:", missing_columns)
    print("Please check whether you downloaded the correct Marketing Campaign dataset.")
    exit()

# Convert columns to numeric values
for col in required_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Step 4: Handle missing values
df = df.dropna(subset=required_columns)

print("\nMissing Values After Cleaning:")
print(df[required_columns].isnull().sum())

# Step 5: Calculate summary statistics
print("\nSummary Statistics:")
print(df[required_columns].describe())

# Step 6: Calculate total spending
spending_columns = [
    "MntWines",
    "MntFruits",
    "MntMeatProducts",
    "MntFishProducts",
    "MntSweetProducts",
    "MntGoldProds"
]

df["Total_Spending"] = df[spending_columns].sum(axis=1)

print("\nAverage Income:")
print(df["Income"].mean())

print("\nAverage Total Spending:")
print(df["Total_Spending"].mean())

# Step 7: Correlation analysis
correlation = df[required_columns].corr()

print("\nCorrelation Matrix:")
print(correlation)

# Step 8: Create correlation heatmap
plt.figure(figsize=(10, 7))
sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Customer Income and Product Spending Correlation")
plt.tight_layout()
plt.savefig("campaign_correlation_heatmap.png")
plt.show()

# Step 9: Create income vs total spending scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(
    df["Income"],
    df["Total_Spending"],
    alpha=0.5
)
plt.xlabel("Income")
plt.ylabel("Total Spending")
plt.title("Customer Income vs Total Product Spending")
plt.tight_layout()
plt.savefig("campaign_income_spending.png")
plt.show()

# Step 10: Display top 10 customers by spending
top_customers = df.nlargest(10, "Total_Spending")

print("\nTop 10 Customers by Total Spending:")
print(top_customers[["Income", "Total_Spending"]])

print("\nAnalysis completed successfully!")
print("Heatmap saved as campaign_correlation_heatmap.png")
print("Scatter plot saved as campaign_income_spending.png")
