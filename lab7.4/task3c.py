try:
    with open("example.txt", "w") as f:
        f.write("Hello, World!")
    print("example.txt written successfully")
except IOError as e:
    print(f"Error writing to example.txt: {e}")

try:
    with open("data1.txt", "w") as f1:
        f1.write("First file content\n")
    print("data1.txt written successfully")
except IOError as e:
    print(f"Error writing to data1.txt: {e}")

try:
    with open("data2.txt", "w") as f2:
        f2.write("Second file content\n")
    print("data2.txt written successfully")
except IOError as e:
    print(f"Error writing to data2.txt: {e}")

print("Files written successfully")
try:
    with open("input.txt", "r") as data:
        lines = data.readlines()
    print("input.txt read successfully")
except FileNotFoundError:
    print("Error: input.txt not found")
    lines = []
except IOError as e:
    print(f"Error reading input.txt: {e}")
    lines = []

try:
    with open("output.txt", "w") as output:
        for line in lines:
            output.write(line.upper())
    print("output.txt written successfully")
except IOError as e:
    print(f"Error writing to output.txt: {e}")

print("Processing data")

# Process numbers and calculate squares with error handling
try:
    with open("numbers.txt", "r") as f:
        nums = f.readlines()
    print("numbers.txt read successfully")
except FileNotFoundError:
    print("Error: numbers.txt not found")
    nums = []
except IOError as e:
    print(f"Error reading numbers.txt: {e}")
    nums = []

squares = []
for n in nums:
    n = n.strip()
    if n.isdigit():
        squares.append(int(n) * int(n))
    else:
        print(f"Warning: '{n}' is not a valid number")

try:
    with open("squares.txt", "w") as f2:
        for sq in squares:
            f2.write(str(sq) + "\n")
    print("squares.txt written successfully")
except IOError as e:
    print(f"Error writing to squares.txt: {e}")