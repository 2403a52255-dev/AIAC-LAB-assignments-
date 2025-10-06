def read_file(filename):
    try:
        with open(filename, "r") as f:
            data = f.read()
        return data
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError as e:
        print(f"IO error occurred while reading '{filename}': {e}")
    return None

# Example usage and output display
if __name__ == "__main__":
    # Try reading an existing file
    print("Reading 'example.txt':")
    content = read_file("example.txt")
    if content is not None:
        print(content)
    print()

    # Try reading a non-existent file
    print("Reading 'nonexistent.txt':")
    content = read_file("nonexistent.txt")
    if content is not None:
        print(content)




