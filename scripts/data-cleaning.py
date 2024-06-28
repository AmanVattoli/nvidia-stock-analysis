import pandas as pd

# Load the dataset
file_path = 'nvda_stock_data.csv'  # Using raw string
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(data.head())

# Check for missing values and data types
print(data.isnull().sum())
print(data.dtypes)

# Drop rows with missing values
data.dropna(inplace=True)

# Convert the 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Verify the change
print(data.dtypes)

# Check for duplicate rows
print(data.duplicated().sum())

# Remove duplicate rows
data.drop_duplicates(inplace=True)

# Display the first few rows of the cleaned dataset
print(data.head())

# Save the cleaned dataset to a new CSV file
cleaned_file_path = 'cleaned_nvda_stock_data.csv'
data.to_csv(cleaned_file_path, index=False)

print(f"Cleaned data saved to {cleaned_file_path}")