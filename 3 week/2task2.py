def rectangle_area(length, width):
    return length * width

for i in range(1, 4):
    length, width = map(float, input().split())
    area = rectangle_area(length, width)
    print("Rectangle", i, "area:", area)
