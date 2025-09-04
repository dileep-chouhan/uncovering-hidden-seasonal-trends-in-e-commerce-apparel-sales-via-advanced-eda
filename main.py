import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
# --- 1. Synthetic Data Generation ---
np.random.seed(42) # for reproducibility
# Generate dates for 2 years
dates = pd.date_range(start='2022-01-01', periods=730)
# Create a DataFrame with apparel subcategories and sales data
data = {
    'Date': dates,
    'Category': np.random.choice(['Shirts', 'Pants', 'Dresses', 'Sweaters'], size=730),
    'Sales': np.random.randint(50, 1000, size=730)
}
# Introduce seasonality (example: higher sales in fall/winter for sweaters)
for i in range(len(data['Date'])):
    month = data['Date'][i].month
    if data['Category'][i] == 'Sweaters':
        if month in [9, 10, 11, 12, 1, 2]:  # Fall/Winter months
            data['Sales'][i] += np.random.randint(100, 300) #Increase sales
df = pd.DataFrame(data)
# --- 2. Data Cleaning and Preparation ---
# Convert 'Date' column to datetime if not already
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year
# --- 3. Analysis ---
# Calculate monthly average sales per category
monthly_sales = df.groupby(['Year', 'Month', 'Category'])['Sales'].mean().reset_index()
# --- 4. Visualization ---
plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_sales, x='Month', y='Sales', hue='Category')
plt.title('Monthly Average Sales Trend by Apparel Category')
plt.xlabel('Month')
plt.ylabel('Average Sales')
plt.xticks(range(1,13))
plt.grid(True)
plt.tight_layout()
# Save the plot to a file
output_filename = 'monthly_sales_trend_by_category.png'
plt.savefig(output_filename)
print(f"Plot saved to {output_filename}")
#Further analysis (example: seasonal decomposition) could be added here.  This is a basic example.
#Example of additional analysis:  Seasonal Decomposition using statsmodels (requires additional library)
#import statsmodels.api as sm
#decomposition = sm.tsa.seasonal_decompose(monthly_sales[monthly_sales['Category'] == 'Sweaters']['Sales'], model='additive')
#decomposition.plot()
#plt.savefig('seasonal_decomposition.png')
#print("Seasonal decomposition plot saved to seasonal_decomposition.png")