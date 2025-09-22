# Function to read lines from a file whose name is given by user input
def read_file_lines():
    filename = input("Enter the filename: ")
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            print("File contents:")
            for line in lines:
                print(line, end='')  # end='' to avoid double newlines
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")

# Call the function
read_file_lines()