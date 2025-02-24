import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ✅ Load dataset
file_path = r"C:\Users\hp\Desktop\Intern_projects\Coffee_Sales_Analysis\Coffee_Sales_Analysis\data\index.csv"
df = pd.read_csv(file_path)

# ✅ Convert 'date' & 'datetime' column to proper datetime format
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['datetime'] = pd.to_datetime(df['datetime'], errors='coerce')

# ✅ Extract 'hour' & 'day_of_week' for analysis
df['hour'] = df['datetime'].dt.hour
df['day_of_week'] = df['date'].dt.day_name()

# ✅ Aggregate total sales per day & hour
sales_by_day = df.groupby("day_of_week")["money"].sum().reindex([
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
])
sales_by_hour = df.groupby("hour")["money"].sum()

# ✅ Plot Daily Sales Trend
plt.figure(figsize=(10, 5))
sns.barplot(x=sales_by_day.index, y=sales_by_day.values, palette="Blues")
plt.xlabel("Day of the Week")
plt.ylabel("Total Sales")
plt.title("Daily Sales Trend")
plt.xticks(rotation=45)
plt.show()

# ✅ Plot Hourly Sales Trend
plt.figure(figsize=(10, 5))
sns.lineplot(x=sales_by_hour.index, y=sales_by_hour.values, marker="o", color="r")
plt.xlabel("Hour of the Day")
plt.ylabel("Total Sales")
plt.title("Hourly Sales Trend")
plt.grid()
plt.xticks(range(0, 24))
plt.show()
