import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = r"C:\Users\hp\Desktop\Intern_projects\Coffee_Sales_Analysis\Coffee_Sales_Analysis\data\index.csv"
data = pd.read_csv(file_path)

# Convert date column to datetime format
data['date'] = pd.to_datetime(data['date'], dayfirst=True)

# Plot sales distribution
plt.figure(figsize=(10, 5))
sns.barplot(x='coffee_name', y='money', data=data, estimator=sum, ci=None)
plt.xlabel("Coffee Type")
plt.ylabel("Total Sales")
plt.title("Total Sales of Each Coffee Type")
plt.xticks(rotation=45)
plt.show()
