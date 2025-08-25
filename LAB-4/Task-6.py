import csv
import os

def analyze_csv_file(file_path):
    """
    Reads a CSV file and returns statistics about the data.
    
    Args:
        file_path (str): Path to the CSV file to analyze
        
    Returns:
        dict: Dictionary containing:
            - total_rows: Total number of rows in the file
            - empty_rows: Number of rows that are completely empty
            - total_words: Total number of words across all cells in the file
            
    Raises:
        FileNotFoundError: If the CSV file doesn't exist
        Exception: For other file reading errors
    """
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found")
    
    total_rows = 0
    empty_rows = 0
    total_words = 0
    
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            
            for row in csv_reader:
                total_rows += 1
                
                # Check if row is empty (all cells are empty or whitespace)
                is_empty = True
                row_words = 0
                
                for cell in row:
                    if cell.strip():  # If cell has non-whitespace content
                        is_empty = False
                        # Count words in this cell
                        words = cell.strip().split()
                        row_words += len(words)
                
                if is_empty:
                    empty_rows += 1
                
                total_words += row_words
                
    except Exception as e:
        raise Exception(f"Error reading CSV file: {str(e)}")
    
    return {
        'total_rows': total_rows,
        'empty_rows': empty_rows,
        'total_words': total_words
    }

def print_analysis_results(results):
    """
    Prints the analysis results in a formatted way.
    
    Args:
        results (dict): Results from analyze_csv_file function
    """
    print("CSV File Analysis Results:")
    print("-" * 30)
    print(f"Total rows: {results['total_rows']}")
    print(f"Empty rows: {results['empty_rows']}")
    print(f"Total words: {results['total_words']}")

# Example usage and testing
if __name__ == "__main__":
    # Example 1: Test with user input
    try:
        file_path = input("Enter the path to your CSV file: ").strip()
        if file_path:
            results = analyze_csv_file(file_path)
            print_analysis_results(results)
        else:
            print("No file path provided.")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 2: Create a sample CSV file for testing
    print("\n" + "="*50)
    print("Creating a sample CSV file for testing...")
    
    sample_data = [
        ["Name", "Age", "City"],
        ["John Doe", "25", "New York"],
        ["", "", ""],  # Empty row
        ["Jane Smith", "30", "Los Angeles"],
        ["Bob Johnson", "", "Chicago"],  # Row with some empty cells
        ["", "", ""],  # Another empty row
        ["Alice Brown", "28", "Boston"]
    ]
    
    sample_file = "sample_data.csv"
    try:
        with open(sample_file, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerows(sample_data)
        
        print(f"Sample CSV file '{sample_file}' created successfully!")
        print("Sample data:")
        for row in sample_data:
            print(f"  {row}")
        
        # Analyze the sample file
        print(f"\nAnalyzing '{sample_file}':")
        results = analyze_csv_file(sample_file)
        print_analysis_results(results)
        
    except Exception as e:
        print(f"Error creating sample file: {e}")
