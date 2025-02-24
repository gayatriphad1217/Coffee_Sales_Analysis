import matplotlib.pyplot as plt
import pandas as pd

# Correct file path for Windows
file_path = r"C:\Users\hp\Desktop\Intern_projects\Coffee_Sales_Analysis\Coffee_Sales_Analysis\data\index.csv"

# Read dataset
data = pd.read_csv(file_path)  

# Grouping Data
sales_per_coffee = data.groupby("coffee_name")["money"].sum()

# Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(sales_per_coffee, labels=sales_per_coffee.index, autopct='%1.1f%%', 
        startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])

plt.title("Sales Distribution of Coffee Types")
plt.show()
