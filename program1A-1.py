import pandas as pd
# Online CSV dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
# CSV file reading
df = pd.read_csv(url)
# Displaying the first five rows
print("First five rows of the dataset:")
print(df.head())
# Displaying dataset information
print("\nDataset Information:")
print(df.info())
# Displaying the shape of the dataset
print("\nNumber of rows and columns:")
print(df.shape)