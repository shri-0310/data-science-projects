# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the Dataset
file_path = 'sales_data.csv'  # Replace with your file path
sales_data = pd.read_csv(file_path)

# Inspect the dataset
print("First 5 rows of the dataset:")
print(sales_data.head())
print("\nDataset Info:")
print(sales_data.info())

# Step 2: Data Cleaning
# Remove duplicates
sales_data.drop_duplicates(inplace=True)

# Handle missing values
sales_data.fillna(0, inplace=True)

# Convert date column to datetime (if applicable)
sales_data['Date'] = pd.to_datetime(sales_data['Date'])

# Confirm the cleaning process
print("\nCleaned Dataset:")
print(sales_data.head())

# Step 3: Calculate Key Metrics
# Total Sales
total_sales = sales_data['Sales'].sum()
print(f"\nTotal Sales: {total_sales}")

# Average Sales
average_sales = sales_data['Sales'].mean()
print(f"Average Sales: {average_sales}")

# Sales Trends Over Time
sales_trends = sales_data.groupby('Date')['Sales'].sum()
print("\nSales Trends Over Time:")
print(sales_trends)

# Step 4: Visualize Sales Trends
plt.figure(figsize=(10, 6))
sales_trends.plot(kind='line', marker='o', color='blue')
plt.title('Sales Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.grid()
plt.show()

# Step 5: Identify Top-Performing Products
# Group data by Product and sum sales
top_products = sales_data.groupby('Product')['Sales'].sum().sort_values(ascending=False)
print("\nTop 10 Performing Products:")
print(top_products.head(10))

# Bar chart for Top 10 Products
plt.figure(figsize=(10, 6))
top_products.head(10).plot(kind='bar', color='orange')
plt.title('Top 10 Performing Products')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.show()

# Step 6: Identify Top-Performing Regions (Optional)
# Group data by Region and sum sales
top_regions = sales_data.groupby('Region')['Sales'].sum().sort_values(ascending=False)
print("\nTop Performing Regions:")
print(top_regions)

# Bar chart for Top Performing Regions
plt.figure(figsize=(10, 6))
top_regions.plot(kind='bar', color='purple')
plt.title('Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.show()