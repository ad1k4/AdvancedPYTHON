def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

A, B, C, D = map(int, input().split())

num = A * D
den = B * C

g = gcd(num, den)
num //= g
den //= g

print(f"{num}/{den}")
