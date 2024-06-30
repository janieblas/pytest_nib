# triangle.py

def calculate_triangle_area(base, height):
    """
    Calculate the area of a triangle given its base and height.

    Parameters:
    - base (float or int): Base of the triangle.
    - height (float or int): Height of the triangle.

    Returns:
    - float: Calculated area of the triangle.
    """
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive and greater than zero.")
    
    area = 0.5 * base * height
    return area

"""
# Example usage
if __name__ == "__main__":
    base = 5
    height = 3
    area = calculate_triangle_area(base, height)
    print(f"The area of the triangle with base {base} and height {height} is: {area}")
"""