
# Data Cleaning and Preparation with Python Workshop

## Sample Dataset:
Let’s use a hypothetical dataset representing customer orders. It has common issues like missing values, duplicates, and incorrect data formats.

| Order_ID | Customer_Name | Order_Date | Order_Amount | Product_Category | Email              | Country  |
|----------|---------------|------------|--------------|------------------|--------------------|----------|
| 1        | Alice Smith    | 2024-01-15 | 150.5        | Electronics       | alice@example.com   | USA      |
| 2        | Bob Johnson    | 2024-02-20 |              | Furniture         |                    | UK       |
| 3        | Alice Smith    | 2024-01-15 | 150.5        | Electronics       | alice@example.com   | USA      |
| 4        | Charlie Lee    | Invalid    | 300.25       | Clothing          | charlie@example.com | Canada   |
| 5        | Emma Davis     | 2024-03-01 | 100.75       | Invalid           | emma@example.com    |          |

### Dataset Issues:
- Missing values in `Order_Amount`, `Email`, and `Country` columns.
- Duplicates (see rows 1 and 3).
- Incorrect data in `Order_Date` and `Product_Category` columns.

---

## Sample Code:

```python
# Import necessary libraries
import pandas as pd
import numpy as np

# Sample data
data = {
    "Order_ID": [1, 2, 3, 4, 5],
    "Customer_Name": ["Alice Smith", "Bob Johnson", "Alice Smith", "Charlie Lee", "Emma Davis"],
    "Order_Date": ["2024-01-15", "2024-02-20", "2024-01-15", "Invalid", "2024-03-01"],
    "Order_Amount": [150.5, np.nan, 150.5, 300.25, 100.75],
    "Product_Category": ["Electronics", "Furniture", "Electronics", "Clothing", "Invalid"],
    "Email": ["alice@example.com", np.nan, "alice@example.com", "charlie@example.com", "emma@example.com"],
    "Country": ["USA", "UK", "USA", "Canada", np.nan]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the raw data
print("Raw Data:")
print(df)

# 1. Handling Missing Data
print("\nStep 1: Handling Missing Data")
# Fill missing values in 'Order_Amount' with the mean
df['Order_Amount'].fillna(df['Order_Amount'].mean(), inplace=True)

# Fill missing 'Email' with a default string and 'Country' with 'Unknown'
df['Email'].fillna("no_email@example.com", inplace=True)
df['Country'].fillna("Unknown", inplace=True)

print(df)

# 2. Remove Duplicates
print("\nStep 2: Removing Duplicates")
df.drop_duplicates(inplace=True)
print(df)

# 3. Correcting Data Formats
print("\nStep 3: Correcting Data Formats")

# Convert 'Order_Date' to datetime, setting invalid parsing to NaT (Not a Time)
df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce')

# Replace invalid categories in 'Product_Category'
df['Product_Category'].replace('Invalid', 'Unknown', inplace=True)

print(df)

# 4. Detecting and Handling Outliers (if any)
print("\nStep 4: Detecting and Handling Outliers")

# Define simple outlier threshold for 'Order_Amount' (greater than 500 is considered an outlier here)
outlier_threshold = 500
df.loc[df['Order_Amount'] > outlier_threshold, 'Order_Amount'] = np.nan

print(df)

# 5. Basic Exploratory Data Analysis
print("\nStep 5: Exploratory Data Analysis")
# Summary statistics
print(df.describe())

# Basic visualizations can also be added using libraries like Matplotlib or Seaborn for data insights.
```

---

### Explanation of Code:

1. **Handling Missing Data**:
   - `Order_Amount`: Filled missing values with the column's mean.
   - `Email`: Filled missing values with a placeholder string.
   - `Country`: Filled missing values with "Unknown."

2. **Removing Duplicates**:
   - Identified and removed duplicate rows (like rows 1 and 3 in the dataset).

3. **Correcting Data Formats**:
   - Converted `Order_Date` to a datetime format, and invalid dates were set to `NaT` (Not a Time).
   - Replaced invalid entries in `Product_Category` with "Unknown."

4. **Detecting and Handling Outliers**:
   - Simple outlier detection by defining a threshold for `Order_Amount`. Any value above 500 was treated as an outlier and set to `NaN`.

5. **Exploratory Data Analysis (EDA)**:
   - Basic summary statistics using `describe()`.
   - Further analysis or visualizations (e.g., distribution plots) can be added using `Matplotlib` or `Seaborn`.

### Additional Enhancements for Workshop:
- **Visualization**: Incorporate Matplotlib or Seaborn to show cleaned data distributions (e.g., histograms of `Order_Amount`).
- **Advanced Cleaning Techniques**: Introduce regular expressions for cleaning email formats or text columns.
