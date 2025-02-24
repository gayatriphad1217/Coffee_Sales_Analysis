import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# ✅ Load dataset
file_path = r"C:\Users\hp\Desktop\Intern_projects\Coffee_Sales_Analysis\Coffee_Sales_Analysis\data\index.csv"
df = pd.read_csv(file_path)

# ✅ Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# ✅ Drop NaN values in 'date'
df = df.dropna(subset=['date'])

# ✅ Sort by date
df = df.sort_values(by='date')

# ✅ Use 'money' as sales column
sales_column = 'money'

# ✅ Set 'date' as index for time series analysis
df.set_index('date', inplace=True)

# ✅ Train ARIMA Model (p=5, d=1, q=0)
model = ARIMA(df[sales_column], order=(5,1,0))
model_fit = model.fit()

# ✅ Forecast Next 7 Days
future_forecast = model_fit.forecast(steps=7)
print("Future Sales Forecast for Next 7 Days:")
print(future_forecast)

# ✅ Plot Sales Trend + Future Prediction
plt.figure(figsize=(10,5))
plt.plot(df.index, df[sales_column], label="Past Sales")
plt.plot(pd.date_range(start=df.index[-1], periods=8, freq='D')[1:], future_forecast, label="Predicted Sales", linestyle="dashed", color="red")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.title("Sales Trend & Future Prediction")
plt.legend()
plt.grid()
plt.xticks(rotation=45)
plt.show()
