import matplotlib.pyplot as plt
import pandas as pd

# Read dataset
data = pd.read_csv(r"C:\Users\hp\Desktop\Intern_projects\Coffee_Sales_Analysis\Coffee_Sales_Analysis\data\index.csv", parse_dates=["date"])  # Ensure the date column exists

# Grouping data by date
sales_over_time = data.groupby("date")["money"].sum()

# Plot Time Series
plt.figure(figsize=(10, 5))
plt.plot(sales_over_time.index, sales_over_time.values, marker='o', linestyle='-', color='b', label="Total Sales")

# Formatting
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.title("Coffee Sales Over Time")
plt.xticks(rotation=45)
plt.legend()
plt.grid()

# Show Plot
plt.show()
