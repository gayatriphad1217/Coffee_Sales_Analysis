import pandas as pd
import matplotlib.pyplot as plt

# ✅ Correct file path
file_path = r"C:\Users\hp\Desktop\Intern_projects\Coffee_Sales_Analysis\Coffee_Sales_Analysis\data\index.csv"

# ✅ Load dataset
data = pd.read_csv(file_path)

# ✅ Count cash vs. card transactions
payment_counts = data["cash_type"].value_counts()

# ✅ Plot Pie Chart
plt.figure(figsize=(6, 6))
plt.pie(payment_counts, labels=payment_counts.index, autopct='%1.1f%%', colors=['gold', 'lightblue'])
plt.title("Cash vs. Card Transactions")
plt.show()
