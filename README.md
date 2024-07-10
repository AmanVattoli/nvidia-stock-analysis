# NVIDIA Stock Analysis

This project focuses on analyzing NVIDIA's stock data to understand its performance from 2020 to 2024, identify trends, and visualize key metrics using Tableau.

[View the interactive Tableau dashboard here](https://public.tableau.com/views/NvidiaStocksAnalysis/Dashboard1?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link)

## Steps Taken

### Data Collection
- **Objective**: To analyze historical stock data of NVIDIA.
- **Data Source**: Downloaded historical stock data from Yahoo Finance.
- **File Used**: `nvda_stock_data.csv`

### Data Preprocessing
- **Loading Data**: Loaded the stock data into a pandas DataFrame.
- **Data Cleaning**:
  - Checked for missing values and data types.
  - Dropped rows with missing values.
  - Converted the 'Date' column to datetime format.
  - Checked for and removed duplicate rows.

- **Saving Cleaned Data**: Saved the cleaned dataset to a new CSV file named `cleaned_nvda_stock_data.csv`.

### Data Visualization
- **Tool Used**: Tableau

## Results

Below are the key visualizations from the project.

### Visualizations

#### NVIDIA Stock Closing Prices and 30-Day Moving Average
![NVIDIA Stock Closing Prices and 30-Day Moving Average](https://github.com/AmanVattoli/nvidia-stocks-analysis/assets/119834364/9a9fd395-5011-4269-a84d-0f1c2e17c5ac)

**Analysis**:
- **Upward Slope**: From 2020 to 2024, NVIDIA's stock shows a significant upward trend, indicating strong positive performance.
- **Performance**: NVIDIA's stock has performed exceptionally well, signifying strong investor confidence and company growth.

#### Monthly Trading Volume of NVIDIA Stock
![Monthly Trading Volume of NVIDIA Stock](https://github.com/AmanVattoli/nvidia-stocks-analysis/assets/119834364/32e7bd79-2863-4682-9d33-d881ab650b55)

**Analysis**:
- **Overall Trading Volume Trends**: Noticeable increase in trading volume from 2020 to 2024 with significant fluctuations indicating varying levels of investor activity.
- **High Trading Volume Periods**: Several months with particularly high trading volumes, possibly reflecting market-moving events.
- **Periods of Lower Activity**: Periods with relatively lower trading volumes, indicating quieter trading periods.
