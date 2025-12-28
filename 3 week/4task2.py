def inside_circle(x, y, a, b, r):
    return (x - a) ** 2 + (y - b) ** 2 < r ** 2

a, b, r = map(int, input().split())
p1, p2 = map(int, input().split())
f1, f2 = map(int, input().split())
l1, l2 = map(int, input().split())

count = 0
count += 1 if inside_circle(p1, p2, a, b, r) else 0
count += 1 if inside_circle(f1, f2, a, b, r) else 0
count += 1 if inside_circle(l1, l2, a, b, r) else 0

print(count)
