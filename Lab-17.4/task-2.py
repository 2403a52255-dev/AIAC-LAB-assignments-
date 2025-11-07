import pandas as pd

# Load the dataset
df = pd.read_csv('sales_transactions.csv')

# Convert transaction dates to proper datetime format
df['transaction_date'] = pd.to_datetime(df['transaction_date'], errors='coerce')

# Create a new column for "Month-Year"
df['Month-Year'] = df['transaction_date'].dt.to_period('M')

# Remove rows with negative or zero transaction amounts
df = df[df['transaction_amount'] > 0]

# Normalize the "transaction_amount" column using Min-Max scaling
df['normalized_transaction_amount'] = (df['transaction_amount'] - df['transaction_amount'].min()) / (df['transaction_amount'].max() - df['transaction_amount'].min())

# Output the preprocessed DataFrame
print(df)