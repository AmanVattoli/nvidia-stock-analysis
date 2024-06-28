import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
cleaned_file_path = 'cleaned_nvda_stock_data.csv'
data = pd.read_csv(cleaned_file_path, parse_dates=['Date'], index_col='Date')

# Plot a scatter plot of Volume vs Close price with a regression line
plt.figure(figsize=(10, 6))
sns.regplot(x='Volume', y='Close', data=data, scatter_kws={'color': 'red'}, line_kws={'color': 'blue'})
plt.xlabel('Volume')
plt.ylabel('Close Price')
plt.title('Scatter Plot of Volume vs Close Price with Regression Line')
plt.show()

print(data[['Volume', 'Close']].corr())