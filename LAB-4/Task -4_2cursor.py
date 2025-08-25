import csv

def analyze_csv(file_path):
    total_rows = 0
    empty_rows = 0
    word_count = 0

    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            total_rows += 1
            if all(cell.strip() == '' for cell in row):
                empty_rows += 1
            for cell in row:
                word_count += len(cell.split())

    return total_rows, empty_rows, word_count

if __name__ == "__main__":
    file_path = "a.csv"
    total, empty, words = analyze_csv(file_path)
    print(f"Total rows: {total}")
    print(f"Empty rows: {empty}")
    print(f"Total words: {words}")
