def gcd(a, b):
    a = abs(a)
    while b:
        a, b = b, a % b
    return a

A, B, C, D = map(int, input().split())

num = A * D - C * B
den = B * D

g = gcd(num, den)
num //= g
den //= g

if den < 0:
    num = -num
    den = -den

print(f"{num}/{den}")
