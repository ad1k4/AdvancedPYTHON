import math

def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

a1, b1 = 3, 4
a2, b2 = 5, 12

hypotenuse1 = calculate_hypotenuse(a1, b1)
hypotenuse2 = calculate_hypotenuse(a2, b2)

print("Hypotenuse of triangle 1:", hypotenuse1)
print("Hypotenuse of triangle 2:", hypotenuse2)

if hypotenuse1 > hypotenuse2:
    print("The hypotenuse of triangle 1 is greater.")
else:
    print("The hypotenuse of triangle 2 is greater.")
