def temperature_conversion():
    """
    Converts temperature between Celsius, Fahrenheit, and Kelvin.
    Takes user input for the temperature value and the conversion type.
    """
    print("Temperature Conversion Tool")
    print("Choose the conversion type:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    choice = input("Enter your choice (1-6): ").strip()

    if choice not in {'1', '2', '3', '4', '5', '6'}:
        print("Invalid choice. Please select a number from 1 to 6.")
        return

    try:
        temp = float(input("Enter the temperature value: ").strip())
    except ValueError:
        print("Invalid temperature value. Please enter a numeric value.")
        return

    if choice == '1':
        # Celsius to Fahrenheit
        result = (temp * 9/5) + 32
        print(f"{temp}°C = {result:.2f}°F")
    elif choice == '2':
        # Fahrenheit to Celsius
        result = (temp - 32) * 5/9
        print(f"{temp}°F = {result:.2f}°C")
    elif choice == '3':
        # Celsius to Kelvin
        result = temp + 273.15
        print(f"{temp}°C = {result:.2f}K")
    elif choice == '4':
        # Kelvin to Celsius
        result = temp - 273.15
        print(f"{temp}K = {result:.2f}°C")
    elif choice == '5':
        # Fahrenheit to Kelvin
        result = (temp - 32) * 5/9 + 273.15
        print(f"{temp}°F = {result:.2f}K")
    elif choice == '6':
        # Kelvin to Fahrenheit
        result = (temp - 273.15) * 9/5 + 32
        print(f"{temp}K = {result:.2f}°F")
1
# Example usage:
temperature_conversion()


