def rectangle_area(x, y):
    return x * y

def square_area(x):
    return x * x

def circle_area(x):
    return 3.14 * x * x

def calculate_area(shape, x, y=0):
    area_functions = {
        "rectangle": lambda x, y: rectangle_area(x, y),
        "square": lambda x, _: square_area(x),
        "circle": lambda x, _: circle_area(x)
    }
    if shape not in area_functions:
        raise ValueError(f"Unknown shape: {shape}")
    return area_functions[shape](x, y)

# Example usage and output display
if __name__ == "__main__":
    print("Rectangle area (5, 3):", calculate_area("rectangle", 5, 3))
    print("Square area (4):", calculate_area("square", 4))
    print("Circle area (2):", calculate_area("circle", 2))



