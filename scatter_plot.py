import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# CSV file ka path
file_path = r"C:\Users\hp\Desktop\Intern_projects\Coffee_Sales_Analysis\Coffee_Sales_Analysis\data\index.csv"

# Data load karo
data = pd.read_csv(file_path)

# Scatter plot banane ke liye
plt.figure(figsize=(8,5))
sns.scatterplot(x=data['date'], y=data['money'], hue=data['cash_type'])
plt.xlabel('Date')
plt.ylabel('Sales (Money)')
plt.title('Coffee Sales Scatter Plot')
plt.xticks(rotation=45)
plt.show()
