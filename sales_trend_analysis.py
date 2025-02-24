import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file with correct absolute path
file_path = r"C:\Users\hp\Desktop\Intern_projects\Coffee_Sales_Analysis\Coffee_Sales_Analysis\data\index.csv"
df = pd.read_csv(file_path)

# Print available columns
print("Columns in CSV:", df.columns)

# Strip spaces and convert column names to lowercase for consistency
df.columns = df.columns.str.strip().str.lower()

# Check if 'date' column exists after processing
if 'date' not in df.columns:
    raise KeyError(f"Column 'Date' not found in the dataset. Available columns: {df.columns}")

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Drop rows where 'date' conversion failed
df = df.dropna(subset=['date'])

# Sort by date
df = df.sort_values(by='date')

# Debugging: Print available columns again
print("Updated column names:", df.columns)

# Find a suitable column for sales
sales_column = None
for col in df.columns:
    if "sales" in col or "revenue" in col:
        sales_column = col
        break

if sales_column is None:
    raise KeyError(f"No suitable 'total_sales' column found. Available columns: {df.columns}")

# Plot Sales Trend
plt.figure(figsize=(10, 5))
plt.plot(df['date'], df[sales_column], marker='o', linestyle='-', color='b')
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.title("Sales Trend Analysis")
plt.grid(True)
plt.xticks(rotation=45)
plt.show()
