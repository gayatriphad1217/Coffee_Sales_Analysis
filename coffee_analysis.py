import pandas as pd

file_path = r"C:\Users\hp\Desktop\Intern_projects\Coffee_Sales_Analysis\Coffee_Sales_Analysis\data\index.csv"
data = pd.read_csv(file_path)

# Data Overview
print(data.info())  # Check columns & data types
print(data.describe())  # Summary statistics
print(data.head())  # First few rows

