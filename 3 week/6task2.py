import math

def heron(x, y, z):
    s = (x + y + z) / 2.0
    return math.sqrt(s * (s - x) * (s - y) * (s - z))

a, b, c, d, diag = map(float, input().split())

area = heron(a, b, diag) + heron(c, d, diag)
print(f"{area:.6f}")
