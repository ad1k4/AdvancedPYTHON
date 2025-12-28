def rectangle_area(a, b):
    return a * b

def right_triangle_area(a, b):
    return a * b / 2

x, y, z, t = map(float, input().split())

area = rectangle_area(x, y) + right_triangle_area(z, t)
print(f"{area:.6f}")
