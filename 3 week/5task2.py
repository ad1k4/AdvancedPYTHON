n = int(input())

small = []
large = []

i = 1
while i * i <= n:
    if n % i == 0:
        small.append(i)
        if i != n // i:
            large.append(n // i)
    i += 1

divs = small + large[::-1]
print(*divs)
