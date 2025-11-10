import pandas as pd
import numpy as np

# Generate sample dirty dataset
def create_sample_dataset():
    # Create sample data with duplicates and NaN values
    data = {
        'Customer ID': [1, 2, 2, 3, 4, 5, None, 5],
        'First_Name': ['John', 'Jane', 'Jane', 'Bob', None, 'Alice', 'Tom', 'Alice'],
        'Last name': ['Smith', 'Doe', 'Doe', 'Johnson', 'Brown', 'Wilson', 'Clark', 'Wilson'],
        'Age': [25, 30, 30, None, 45, 35, 28, 35],
        'SALARY': [50000, 60000, 60000, 75000, None, 65000, 55000, 65000]
    }
    
    df = pd.DataFrame(data)
    # Save the dirty dataset
    df.to_csv('sample_dirty_dataset.csv', index=False)
    return df

def clean_dataset(df):
    # 1. Standardize column names
    df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('-', '_')
    
    # 2. Remove duplicates
    print("\nNumber of duplicates:", df.duplicated().sum())
    df = df.drop_duplicates()
    
    # 3. Handle NaN values
    print("\nNaN values before cleaning:")
    print(df.isnull().sum())
    
    # Fill numeric columns with median
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    for col in numeric_columns:
        df[col] = df[col].fillna(df[col].median())
    
    # Fill categorical columns with mode
    categorical_columns = df.select_dtypes(include=['object']).columns
    for col in categorical_columns:
        df[col] = df[col].fillna(df[col].mode()[0])
    
    print("\nNaN values after cleaning:")
    print(df.isnull().sum())
    
    return df

def main():
    # Create and load the sample dataset
    print("Creating sample dirty dataset...")
    original_df = create_sample_dataset()
    print("\nOriginal Dataset:")
    print(original_df)
    
    # Clean the dataset
    print("\nCleaning dataset...")
    cleaned_df = clean_dataset(original_df)
    
    # Save cleaned dataset
    cleaned_df.to_csv('cleaned_dataset.csv', index=False)
    
    print("\nCleaned Dataset:")
    print(cleaned_df)
    
    print("\nCleaned dataset has been saved as 'cleaned_dataset.csv'")

if __name__ == "__main__":
    main()