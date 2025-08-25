import csv

def analyze_csv(file_path):
    """
    Analyzes a CSV file and returns:
    - Total number of rows
    - Number of empty rows  
    - Total number of words across the file
    """
    total_rows = 0
    empty_rows = 0
    total_words = 0
    
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            total_rows += 1
            
            # Check if row is completely empty
            if all(cell.strip() == '' for cell in row):
                empty_rows += 1
            
            # Count words in all cells
            for cell in row:
                words = cell.strip().split()
                total_words += len(words)
    
    return total_rows, empty_rows, total_words

# Example usage
file_path = input("Enter CSV file path: ")
try:
    rows, empty, words = analyze_csv(file_path)
    print(f"Total rows: {rows}")
    print(f"Empty rows: {empty}")
    print(f"Total words: {words}")
except FileNotFoundError:
    print("File not found!")
except Exception as e:
    print(f"Error: {e}")
