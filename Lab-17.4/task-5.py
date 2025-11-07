import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer

# Read the dataset
def preprocess_financial_data(file_path='financial_raw_dataset.csv'):
    try:
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Handle missing values
        numeric_imputer = SimpleImputer(strategy='mean')
        numeric_columns = ['price', 'volume']
        df[numeric_columns] = numeric_imputer.fit_transform(df[numeric_columns])
        
        # Create moving averages
        df['7_day_ma'] = df.groupby('company_name')['price'].rolling(window=7).mean().reset_index(0, drop=True)
        df['30_day_ma'] = df.groupby('company_name')['price'].rolling(window=30).mean().reset_index(0, drop=True)
        
        # Create additional technical indicators
        df['price_change'] = df.groupby('company_name')['price'].pct_change()
        df['volume_change'] = df.groupby('company_name')['volume'].pct_change()
        
        # Normalize continuous variables
        scaler = StandardScaler()
        continuous_cols = ['price', 'volume', '7_day_ma', '30_day_ma', 'price_change', 'volume_change']
        df[continuous_cols] = scaler.fit_transform(df[continuous_cols])
        
        # Encode categorical variables
        le = LabelEncoder()
        categorical_cols = ['sector', 'company_name']
        for col in categorical_cols:
            df[f'{col}_encoded'] = le.fit_transform(df[col])
            
        # Fill any remaining NaN values (from calculations)
        df = df.fillna(0)
        
        print("Data preprocessing completed successfully!")
        return df
        
    except FileNotFoundError:
        print("Error: Financial dataset file not found!")
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

if __name__ == "__main__":
    # Process the dataset
    processed_df = preprocess_financial_data()
    
    if processed_df is not None:
        # Display info about the processed dataset
        print("\nProcessed Dataset Info:")
        print(processed_df.info())
        
        # Save the processed dataset
        processed_df.to_csv('processed_financial_dataset.csv', index=False)
        print("\nProcessed dataset saved successfully!")