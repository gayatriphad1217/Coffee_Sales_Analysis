import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ✅ Correct file path
file_path = r"C:\Users\hp\Desktop\Intern_projects\Coffee_Sales_Analysis\Coffee_Sales_Analysis\data\index.csv"

# ✅ Load dataset
data = pd.read_csv(file_path)

# ✅ Count each coffee's total sales
coffee_sales = data["coffee_name"].value_counts()

# ✅ Bar Chart for Coffee Sales
plt.figure(figsize=(10, 5))
sns.barplot(x=coffee_sales.index, y=coffee_sales.values, palette="viridis")
plt.xlabel("Coffee Type")
plt.ylabel("Total Sales")
plt.title("Most Popular Coffee Types")
plt.xticks(rotation=45)
plt.show()
