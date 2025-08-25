import csv

def analyze_csv_file(file_path):
    total_rows = 0
    empty_rows = 0
    total_words = 0

    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            total_rows += 1
            # Consider a row empty if all cells are empty or whitespace
            if all(cell.strip() == '' for cell in row):
                empty_rows += 1
            for cell in row:
                # Count words in each cell (split by whitespace)
                total_words += len(cell.split())

    return total_rows, empty_rows, total_words

if __name__ == "__main__":
    for fname in ["a.csv", "b.csv", "c.csv"]:
        total, empty, words = analyze_csv_file(fname)
        print(f"For {fname}: Total rows = {total}, Empty rows = {empty}, Total words = {words}")
