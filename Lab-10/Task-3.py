def calculate_percentage(amount, percentage):
    """
    Calculate the percentage value of a given amount.

    Parameters:
    amount (float or int): The base amount.
    percentage (float or int): The percentage to calculate.

    Returns:
    float: The calculated percentage of the amount.
    """
    return amount * percentage / 100  # Calculate percentage

total_amount = 200  # The base amount
percentage_value = 15  # The percentage to calculate

# Calculate and print the result
result = calculate_percentage(total_amount, percentage_value)
print(result)
