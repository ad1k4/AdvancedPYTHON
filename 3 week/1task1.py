import math

def calculate_area(shape, *dimensions):
    if shape == 'circle':
        radius = dimensions[0]
        return math.pi * radius ** 2
    elif shape == 'rectangle':
        length, width = dimensions
        return length * width
    elif shape == 'triangle':
        base, height = dimensions
        return 0.5 * base * height
    elif shape == 'square':
        side = dimensions[0]
        return side ** 2
    else:
        return "Shape not recognized"

circle_area = calculate_area('circle', 5)
rectangle_area = calculate_area('rectangle', 4, 6)
triangle_area = calculate_area('triangle', 4, 7)
square_area = calculate_area('square', 3)

print(f"Circle area: {circle_area:.2f}")
print(f"Rectangle area: {rectangle_area}")
print(f"Triangle area: {triangle_area}")
print(f"Square area: {square_area}")
