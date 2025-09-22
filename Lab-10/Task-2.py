def calculate_rectangle_area(length, breadth):
    """
    Calculate the area of a rectangle.

    Parameters:
    length (float or int): The length of the rectangle. Must be non-negative.
    breadth (float or int): The breadth of the rectangle. Must be non-negative.

    Returns:
    float: The area of the rectangle.

    Raises:
    ValueError: If length or breadth is negative.
    """
    # Check for negative values
    if length < 0 or breadth < 0:
        raise ValueError("Length and breadth must not be negative.")
    # Calculate area
    area = length * breadth
    return area

# Example usage
length = 10
breadth = 20
try:
    area = calculate_rectangle_area(length, breadth)
    print(f"The area of the rectangle with length {length} and breadth {breadth} is {area}.")
except ValueError as e:
    print(e)


