import pandas as pd

# Load the dataset
df = pd.read_csv('employee_data.csv')

# Handle missing values
df['salary'].fillna(df['salary'].mean(), inplace=True)
df['department'].fillna('Unknown', inplace=True)
df['joining_date'].fillna(df['joining_date'].mode()[0], inplace=True)

# Convert 'joining_date' to datetime format
df['joining_date'] = pd.to_datetime(df['joining_date'], errors='coerce')

# Standardize department names
department_mapping = {
    'HR': 'HR',
    'hr': 'HR',
    'Human Resources': 'HR',
    'IT': 'IT',
    'it': 'IT',
    'Information Technology': 'IT',
    # Add more mappings as needed
}

df['department'] = df['department'].replace(department_mapping)

# Encode categorical variables
df = pd.get_dummies(df, columns=['department', 'job_role'], drop_first=True)

# Display the cleaned DataFrame
print(df.head())