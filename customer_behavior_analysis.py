import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ✅ Load dataset
file_path = r"C:\Users\hp\Desktop\Intern_projects\Coffee_Sales_Analysis\Coffee_Sales_Analysis\data\index.csv"
df = pd.read_csv(file_path)

# ✅ Check available columns
print("Columns in dataset:", df.columns)

# ✅ Find the most frequent customers (Top 10)
top_customers = df['cash_type'].value_counts().head(10)

# ✅ Plot the top customers
plt.figure(figsize=(10, 5))
sns.barplot(x=top_customers.index, y=top_customers.values, palette="coolwarm")
plt.xlabel("Customer ID")
plt.ylabel("Number of Purchases")
plt.title("Top 10 Frequent Customers")
plt.xticks(rotation=45)
plt.show()

# ✅ Find the most purchased coffee per customer
top_customer_id = top_customers.index[0]  # Get the most frequent customer ID
customer_orders = df[df['cash_type'] == top_customer_id]['coffee_name'].value_counts()

# ✅ Plot the favorite coffee of the top customer
plt.figure(figsize=(8, 5))
sns.barplot(x=customer_orders.index, y=customer_orders.values, palette="Blues_r")
plt.xlabel("Coffee Name")
plt.ylabel("Number of Orders")
plt.title(f"Favorite Coffee of Customer: {top_customer_id}")
plt.xticks(rotation=45)
plt.show()
