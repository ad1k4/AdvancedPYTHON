import math

def triangle_area(side):
    height = (math.sqrt(3) / 2) * side
    return 0.5 * side * height

def hexagon_area(side):
    return 6 * triangle_area(side)

side = 5
hex_area = hexagon_area(side)
print("Area of the hexagon:", hex_area)
